from langchain_core.prompts.chat import ChatPromptTemplate, MessagesPlaceholder


# basic system prompt for declaring agent profile
SUMMARY_TEMPLATE = """\
Name: {name}. Summary: {summary}.
"""

_SYSTEM_TEMPLATE = """\
You are a part of a team of agents collaborating to build a website \
based on user requirements. Each agent from your team (including you) \
has a specific expertise and skill set, and has a set of tools at their disposal \
to help them accomplish their tasks.

Here is your profile:
{summary}

You work together with the following colleagues:
{colleague_summaries}

Your task as a team is to create a complete, functional, and visually appealing website \
that meets the user's requirements. You should coordinate with your colleagues, \
leverage your individual strengths, and utilize the available tools to achieve this goal.
"""

SYSTEM_PROMPT = ChatPromptTemplate.from_messages(
    [
        ("system", _SYSTEM_TEMPLATE)
    ]
)


# prompt for making a plan
# TODO
_PLANNING_TEMPLATE = ...

PLANNING_PROMPT = ChatPromptTemplate.from_messages(
    [
        MessagesPlaceholder(variable_name="system_message"),
        ("human", _PLANNING_TEMPLATE),
        MessagesPlaceholder(variable_name="messages")
    ]
)


# prompt for voting on the best plan
# TODO
_VOTING_TEMPLATE = ...


VOTING_PROMPT = ...


# ReACT prompts
# TODO
_REACT_PLAN_NEXT_TEMPLATE = ...


REACT_PLAN_NEXT_PROMPT = ...