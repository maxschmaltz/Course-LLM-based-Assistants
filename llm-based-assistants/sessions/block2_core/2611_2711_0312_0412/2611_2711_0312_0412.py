from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langgraph.graph import StateGraph, END
from langgraph.graph.message import add_messages
from langgraph.types import Command, Send
from pydantic import BaseModel
from typing import Annotated, List
from typing_extensions import TypedDict
import json
from collections import defaultdict

from agents import init_llm, create_agent
from agents.tools import TOOLS, create_task_description_handoff_tool
from agents.prompts import (
    SUMMARY_TEMPLATE,
    SYSTEM_PROMPT,
    PLANNING_PROMPT,
    VOTING_PROMPT
)
from agents.schemas import (
    Plan,
    PlanGrading
)


class State(TypedDict):
    # at the first stage of the system execution,
    # the agents will be generating and assessing plans
    plans: List[Plan]
    plan_gradings: List[PlanGrading]
    # then, when the plan will be negotiated,
    # the agents will start working on the plan in a
    # decentralized manner so we need to keep track of the
    # conversational history
    messages: Annotated[List[BaseMessage], add_messages]


class WebsiteGenerationLaMA:

    _graph_path = "./webgeneration.png"
    
    def __init__(self):
        self._init_agents() # initialized agents
        self._build()   # build the graph
        self._save_graph()

    def _init_agents(self):
        # load agents JSON  
        with open("agents/agent_items.json") as f:
            agent_items = json.load(f)
        # initialize handoff tools for each agent
        # TODO
        # we will be saving the agents in a dict
        self.agents = {}
        for i, agent_item in enumerate(agent_items):
            # TODO: initialize LLMs, ReACT agents with tools, system messages
            pass

    def _build(self):
        # graph builder
        self._graph_builder = StateGraph(State)
        # add the nodes
        # TODO
        # define edges;
        # TODO
        # compile the graph
        self._compile()

    def _compile(self):
        self.lama = self._graph_builder.compile()

    def _input_node(self, state: State) -> dict:
        user_query = input("Your message: ")
        human_message = HumanMessage(content=user_query)
        # add the input to the messages
        return {
            "messages": human_message   # this will append the input to the messages
        }

    def _plan_node(self, state: State) -> dict:
        # TODO
        return {
            "plans": ...
        }
    
    def _vote_node(self, state: State) -> dict:
        # TODO
        return {
            "plan_gradings": ...
        }

    def _after_vote_node(self, state: State) -> Command:
        # TODO
        if ... >= 17:   # at least 8 and 9
            # TODO
            return Command(
                goto=Send(..., ...),   # start executing the plan
            )
        else:
            # need another round of planning
            return Command(goto="plan")

    def _approval_node(self, state: State) -> Command:
        return Command(
            goto="END",
            update={
                "messages": AIMessage(content="The plan has been approved.")
            }
        )

    def _save_graph(self):
        self.lama.get_graph().draw_mermaid_png(
            output_file_path=self._graph_path
        )

    def run(self):
        input = {
            "plans": [],
            "plan_gradings": [],
            "messages": []
        }
        shown_messages = []
        for event in self.lama.stream(
            input,
            config={"recursion_limit": 250},
            stream_mode="values"
        ):
            if event["messages"]:
                for message in event["messages"]:
                    if not message.id in shown_messages:
                        shown_messages.append(message.id)
                        message.pretty_print()
                        print("\n")
            if event.get("plans"):
                print("================================= Plans Generated =================================\n\n")
                for plan in event["plans"]:
                    print(self._pydantic2str(plan))
                    print("\n")
            if event.get("plan_gradings"):
                print("================================= Plan Gradings =================================\n\n")
                for plan_grading in event["plan_gradings"]:
                    print(self._pydantic2str(plan_grading))
                    print("\n")


if __name__ == "__main__":
    website_gen = WebsiteGenerationLaMA()
    website_gen.run()