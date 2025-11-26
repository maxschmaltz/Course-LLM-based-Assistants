from langchain_core.messages import BaseMessage
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.tools.base import BaseTool
from langchain_core.tools import render_text_description
from langgraph.graph.state import CompiledStateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import create_react_agent
from typing import List, TypedDict, Annotated

from agents.prompts import REACT_PLAN_NEXT_PROMPT


class ReACTState(TypedDict):
    system_message: list
    messages: Annotated[List[BaseMessage], add_messages]
    # this counter is added by LangGraph automatically
    # but here we declare it explicitly for `create_react_agent`
    remaining_steps: int


def create_agent(
    name: str,
    llm: BaseChatModel,
    tools: List[BaseTool],
    **kwargs
) -> CompiledStateGraph:
    
    """
    Create a ReACT agent with a custom plan next action step.

    Args:
        name (str): The name of the agent.
        llm (BaseChatModel): The language model to use.
        tools (List[BaseTool]): A list of tools available to the agent.
        **kwargs: Additional keyword arguments to pass to LangChain agent creation function.

    Returns:
        CompiledStateGraph: An instance of a ReACT agent.
    """
    
    tools_description = render_text_description(tools)
    
    def plan_next(state: dict) -> dict:
        next_action = (REACT_PLAN_NEXT_PROMPT | llm).invoke({
            **state,
            "tools_description": tools_description
        })
        return {
            "messages": next_action
        }

    return create_react_agent(
        name=name,
        model=llm,
        tools=tools,
        state_schema=ReACTState,
        pre_model_hook=plan_next,
        **kwargs
    )