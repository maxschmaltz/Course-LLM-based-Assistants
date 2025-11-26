import os
from langchain_core.messages import AIMessage, ToolMessage
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun # https://docs.langchain.com/oss/python/integrations/tools/ddg
from langchain_community.agent_toolkits import FileManagementToolkit # https://docs.langchain.com/oss/python/integrations/tools/filesystem
from langgraph.types import Command, Send
from langgraph.prebuilt import InjectedState
from langchain_core.tools import InjectedToolCallId
from tidylib import tidy_document   # http://countergram.github.io/pytidylib/
import requests
from typing import Annotated


# web search tool for the content creator
search_web = DuckDuckGoSearchRun()


# image search tool for the designer
def _download_image(image_url: str, out_path: str) -> str:
    out_dir = os.path.dirname(out_path)
    os.makedirs(out_dir, exist_ok=True)
    with requests.get(image_url, stream=True, timeout=10) as img_resp:
        with open(out_path, "wb") as fh:
            for chunk in img_resp.iter_content(chunk_size=8192):
                if chunk:
                    fh.write(chunk)

    return f"Successfully downloaded to {out_path}"


@tool
def search_image(query: str, color: str, out_path: str) -> str:
    """
    Search for an image using the Unsplash API.

    Args:
        query (str): The search query. Should be a single word with a broader meaning.
        color (str): The color filter for the search.
        out_path (str): The path to save the downloaded image.

    Returns:
        str: The URL of the first image result.
    """
    try:
        response = requests.get(
            url="https://api.unsplash.com/search/photos",
            params={
                # https://unsplash.com/documentation#search
                "query": query,
                "color": color,
                "per_page": 1,
                "client_id": os.environ["UNSPLASH_API_KEY"]
            },
            timeout=10
        )
        data = response.json()
        if data["results"]:
            image_url = data["results"][0]["urls"]["regular"]    # regular size
            return _download_image(image_url, out_path)
        else:
            return "No images found."
    except requests.RequestException as e:
        return f"Could not use the tool. Error: {str(e)}"


# linters for the developer
@tool
def html_linter(html_code: str) -> str:

    """
    Lint HTML code for potential issues.

    Args:
        html_code (str): The HTML code to be linted.

    Returns:
        str: A report of linting issues found in the HTML code.
    """

    _, errors = tidy_document(html_code)
    return errors or "No issues found."


@tool
def css_linter(css_code: str) -> str:

    """
    Lint CSS code for potential issues.

    Args:
        css_code (str): The CSS code to be linted.

    Returns:
        str: A report of linting issues found in the CSS code.
    """

    try:
        response = requests.get(
            url="https://jigsaw.w3.org/css-validator/validator",
            # https://jigsaw.w3.org/css-validator/manual.html
            params={
                "text": css_code,
                "profile": "css3",
                "output": "text/plain"
            },
            timeout=10
        )
        return response.text    # will say if there are no errors
    except requests.RequestException as e:
        return f"Could not use the tool. Error: {str(e)}"


# file management tools for the developer
read_file, write_file = FileManagementToolkit(
    root_dir=".",  # specify the root directory for file operations
    selected_tools=["read_file", "write_file"]
).get_tools()


TOOLS = {
    "search_web": search_web,
    "search_image": search_image,
    "html_linter": html_linter,
    "css_linter": css_linter,
    "read_file": read_file,
    "write_file": write_file
}


# separately, we have handoff tools accessible to all agents
def create_task_description_handoff_tool(agent_name: str):

    name = f"transfer_to_{agent_name}"  # name of the tool

    @tool(name, description="Assign a task to {agent_name} with a specific task description.")
    def handoff_tool(
        # this will be populated by the coordinator;
        # the coordinator will see in the docstring that this
        # tool needs a task description to be passed so it 
        # will generate one as the required parameter
        task_description: str,
        # the `InjectedState` annotation will ensure that the
        # current state will be passed to the tool
        # and this parameter will be ignored by the LLM
        state: Annotated[dict, InjectedState],
        # for ToolMessage, is not passed by the LLM either
        tool_call_id: Annotated[str, InjectedToolCallId]
    ) -> Command:
        
        """
        Delegate the task to another agent with a specific task description. The string \
        task description is required to specify what the target agent should do.

        Args:
            task_description (str): A detailed description of the task to be performed by the target agent.
        """

        # explicitly add a ToolMessage as a confirmation of the handoff
        tool_message = ToolMessage(
            content=f"Successfully transferred to {agent_name}",
            tool_call_id=tool_call_id
        )
        
        # wrap the task description in an AI message (alternatively, you can use a user message)
        task_description_message = AIMessage(content=task_description)

        return Command(
            goto=agent_name,
            update={
                "messages": [tool_message, task_description_message]
            },
            # that says that the required agent is in the parent context
            # (so in the main graph) and not in the local context
            graph=Command.PARENT
        )

    return handoff_tool

def start_approval(
    state: Annotated[dict, InjectedState],
    tool_call_id: Annotated[str, InjectedToolCallId]
) -> Command:
    
    """
    Start the approval process after completing the plan.
    """

    # explicitly add a ToolMessage as a confirmation of the handoff
    tool_message = ToolMessage(
        content="Successfully started the approval process",
        tool_call_id=tool_call_id
    )

    return Command(
        goto="approval",
        update={
            "messages": [tool_message]
        },
        graph=Command.PARENT
    )