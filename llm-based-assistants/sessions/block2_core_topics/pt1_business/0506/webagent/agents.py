import os
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_openai import ChatOpenAI
from langchain_core.rate_limiters import InMemoryRateLimiter
from langchain_community.tools.file_management.write import WriteFileTool
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langgraph.graph import StateGraph, END
from langchain_core.runnables.graph import MermaidDrawMethod
from typing import TypedDict, List
import nest_asyncio
import dotenv

dotenv.load_dotenv()    # that loads the .env file variables into os.environ
nest_asyncio.apply()  # apply nest_asyncio to allow nested event loops

from webagent.prompts import (
    HTML_SYSTEM_PROMPT,
    GENERATE_HTML_PROMPT,
    CSS_SYSTEM_PROMPT,
    GENERATE_CSS_PROMPT,
    JS_SYSTEM_PROMPT,
    GENERATE_JS_PROMPT,
    REFINE_PROMPT,
    STATIC_CHECKER_SYSTEM_PROMPT,
    CHECK_CODES_PROMPT,
    PARSE_FEEDBACK_PROMPT,
    Feedback
)

# choose any model, catalogue is available under https://build.nvidia.com/models
MODEL_NAME = "meta/llama-3.3-70b-instruct"


# State definition
class WebsiteState(TypedDict):
    description: str    # user description of the website
    html: str   # generated HTML code
    css: str    # generated CSS code
    js: str # generated JS code
    messages: List[dict]  # {author: str, target: str, content: str}
    refinements: int    # the number of refinements made so far


class WebLaMA:

    _html_agent_name = "html_agent"
    _css_agent_name = "css_agent"
    _js_agent_name = "js_agent"
    _static_checker_name = "static_checker"
    _all_name = "all"

    def __init__(self, max_refinements: int=5):
        # this rate limiter will ensure we do not exceed the rate limit
        # of 40 RPM given by NVIDIA
        rate_limiter = InMemoryRateLimiter(
            requests_per_second=30 / 60,  # 30 requests per minute to be sure
            check_every_n_seconds=0.1,  # wake up every 100 ms to check whether allowed to make a request,
            max_bucket_size=4,  # controls the maximum burst size
        )
        # self.llm = ChatNVIDIA(
        #     model=MODEL_NAME,
        #     api_key=os.getenv("NVIDIA_API_KEY"), 
        #     temperature=0,   # ensure reproducibility,
        #     rate_limiter=rate_limiter  # bind the rate limiter
        # )
        self.llm = ChatOpenAI(
            model="gpt-4o",
            temperature=0   # ensure reproducibility
        )
        self.write_tool = WriteFileTool(root_dir="./")
        # you can't use both a tool and a structured output
        # so we will haver to additionally parse the feedback
        self._static_checker = self.llm.bind_tools([self.write_tool], tool_choice="auto")
        self._feedback_llm = self.llm.with_structured_output(Feedback)
        self.max_refinements = max_refinements
        self._system_messages = {
            self._html_agent_name: SystemMessage(HTML_SYSTEM_PROMPT),
            self._css_agent_name: SystemMessage(CSS_SYSTEM_PROMPT),
            self._js_agent_name: SystemMessage(JS_SYSTEM_PROMPT),
            self._static_checker_name: SystemMessage(STATIC_CHECKER_SYSTEM_PROMPT)
        }
        self._code_mapping = {
            self._html_agent_name: "html",
            self._css_agent_name: "css",
            self._js_agent_name: "js"
        }
        self._build()  # build the graph

    def _build(self):
        # graph builder
        self._graph_builder = StateGraph(WebsiteState)
        # add the nodes
        self._graph_builder.add_node(self._html_agent_name, self._generate_html)
        self._graph_builder.add_node(self._css_agent_name, self._generate_css)
        self._graph_builder.add_node(self._js_agent_name, self._generate_js)
        self._graph_builder.add_node(self._static_checker_name, self._check_codes)
        self._graph_builder.add_node("refine_code", self._refine_code)
        # define edges
        self._graph_builder.set_entry_point(self._html_agent_name)
        self._graph_builder.add_edge(self._html_agent_name, self._css_agent_name)
        self._graph_builder.add_edge(self._css_agent_name, self._js_agent_name)
        self._graph_builder.add_edge(self._js_agent_name, self._static_checker_name)
        self._graph_builder.add_conditional_edges(
            self._static_checker_name,
            self._route,
            # just for the graph visualization
            path_map={
                "refine_code": "refine_code",
                END: END
            }
        )
        # loop refinement until exits
        self._graph_builder.add_edge("refine_code", self._static_checker_name)
        # compile the graph
        self._pipeline = self._graph_builder.compile()
        # self.draw_graph()

    def draw_graph(self):
        # draw the graphs
        try:
            self._pipeline.get_graph().draw_mermaid_png(
                draw_method=MermaidDrawMethod.PYPPETEER,
                output_file_path="./graph.png",
            )
        except Exception as e:
            pass

    # the agents will only see messages targeted to them or to "all"
    def _get_previous_messages(self, state: WebsiteState, name: str) -> List[dict]:
        """Get messages for a specific agent."""
        messages = [
            # wrap the message content into AIMessage
            # so that it can be processed by the LLM
            AIMessage(message["content"]) for message in state["messages"]
            if message["target"] in [name, self._all_name]
        ]
        # always prepend the system message, it is not stored in the state
        return [self._system_messages[name]] + messages
    
    def _generate_html(self, state: WebsiteState) -> str:
        """Generate HTML code based on the user description."""
        prompt = GENERATE_HTML_PROMPT.format(description=state["description"])
        response = self.llm.invoke([self._system_messages[self._html_agent_name], HumanMessage(prompt)])
        new_message = {
            "author": self._html_agent_name,
            "target": self._all_name,    # let all see its generations
            "content": response.content
        }
        return {
            "html": response.content,
            "messages": state["messages"] + [new_message]
        }
    
    def _generate_css(self, state: WebsiteState) -> str:
        """Generate CSS code based on the user description and HTML code."""
        prompt = GENERATE_CSS_PROMPT.format(
            description=state["description"],
            html_code=state["html"]
        )
        response = self.llm.invoke([self._system_messages[self._css_agent_name], HumanMessage(prompt)])
        new_message = {
            "author": self._css_agent_name,
            "target": self._css_agent_name,    # let it see its own generations
            "content": response.content
        }
        return {
            "css": response.content,
            "messages": state["messages"] + [new_message]
        }
    
    def _generate_js(self, state: WebsiteState) -> str:
        """Generate JS code based on the user description and HTML code."""
        prompt = GENERATE_JS_PROMPT.format(
            description=state["description"],
            html_code=state["html"]
        )
        response = self.llm.invoke([self._system_messages[self._js_agent_name], HumanMessage(prompt)])
        new_message = {
            "author": self._js_agent_name,
            "target": self._js_agent_name,    # let it see its own generations
            "content": response.content
        }
        return {
            "js": response.content,
            "messages": state["messages"] + [new_message]
        }
    
    def _check_codes(self, state: WebsiteState) -> str:    # decision node
        """Check the generated HTML, CSS, and JS code for correctness."""
        if state["refinements"] >= self.max_refinements:
            new_message = {
                "author": self._static_checker_name,
                "target": END,
                "content": "Maximum number of refinements reached. Exiting."
            }
            return {
                "messages": state["messages"] + [new_message]
            }
        prompt = CHECK_CODES_PROMPT.format(
            description=state["description"],
            html_code=state["html"],
            css_code=state["css"],
            js_code=state["js"]
        )
        response = self._static_checker.invoke([HumanMessage(prompt)])
        if response.tool_calls:
            # if the response contains a tool call, it means the codes are correct
            # and we should save them into files
            for tool_call in response.tool_calls:
                # since we have only one tool, we can directly invoke it
                self.write_tool.invoke(tool_call)
            new_message = {
                "author": self._static_checker_name,
                "target": END,
                "content": "Website created. Exiting."
            }
            return {
                "messages": state["messages"] + [new_message]
            }
        # otherwise, we have feedback for the agents
        names = ", ".join([
            self._html_agent_name, self._css_agent_name, self._js_agent_name
        ])
        f_prompt = PARSE_FEEDBACK_PROMPT.format(names=names, feedback=response.content)
        feedback = self._feedback_llm.invoke([HumanMessage(f_prompt)])
        new_message = {
            "author": self._static_checker_name,
            "target": feedback.target,
            "content": feedback.feedback
        }
        return {
            "messages": state["messages"] + [new_message]
        }
    
    def _route(self, state: WebsiteState) -> str:
        """Route the state to the next node based on the feedback."""
        # if the target is END, we are done
        if state["messages"][-1]["target"] == END:
            return END
        # otherwise, we need to refine the code
        return "refine_code"
    
    def _refine_code(self, state: WebsiteState) -> WebsiteState:
        """Refine the code based on the feedback."""
        feedback_message = state["messages"][-1]  # last message is the feedback
        target = feedback_message["target"]  # last message is the feedback
        messages = self._get_previous_messages(state, target)
        prompt = REFINE_PROMPT.format(
            description=state["description"],
            feedback=feedback_message["content"]  # last message is the feedback
        )
        response = self.llm.invoke(messages + [HumanMessage(prompt)])
        new_message = {
            "author": target,
            "target": target if not target == self._html_agent_name else self._all_name,
            "content": response.content
        }
        return {
            self._code_mapping[target]: response.content,
            "messages": state["messages"] + [new_message],
            "refinements": state["refinements"] + 1
        }
    
    def run(self, description):
        input = {
            "description": description,
            "html": None,
            "css": None,
            "js": None,
            "messages": [],
            "refinements": 0
        }
        for event in self._pipeline.stream(input, stream_mode="values"):
            if event["messages"]:
                new_message = event["messages"][-1]
                print(f"========= {new_message["author"].upper()} to {new_message["target"]} =========\n\n")
                print(new_message["content"])
