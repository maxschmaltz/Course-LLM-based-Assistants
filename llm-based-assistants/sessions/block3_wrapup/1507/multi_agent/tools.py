import os
import json
import dotenv
import numpy as np
from pydantic import BaseModel, Field
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_core.rate_limiters import InMemoryRateLimiter
from langchain_core.documents import Document
from langchain_core.messages import HumanMessage, AIMessage
from typing import List

from multi_agent.prompts import (
    TICKET_SYSTEM_PROMPT,
    GENERATE_NEW_TICKET_PROMPT,
    _update_ticket_prompt
)

dotenv.load_dotenv()    # that loads the .env file variables into os.environ

# choose any model, catalogue is available under https://build.nvidia.com/models
MODEL_NAME = "meta/llama-3.3-70b-instruct"

# this rate limiter will ensure we do not exceed the rate limit
# of 40 RPM given by NVIDIA
rate_limiter = InMemoryRateLimiter(
    requests_per_second=30 / 60,  # 30 requests per minute to be sure
    check_every_n_seconds=0.1,  # wake up every 100 ms to check whether allowed to make a request,
    max_bucket_size=4,  # controls the maximum burst size
)
llm = ChatNVIDIA(
    model=MODEL_NAME,
    api_key=os.getenv("NVIDIA_API_KEY"), 
    temperature=0,   # ensure reproducibility,
    rate_limiter=rate_limiter  # bind the rate limiter
)

# load tickets from a JSON file
with open("./tickets.json", "r") as f:
    tickets = json.load(f)


class TicketMessage(BaseModel):
    """
    Represents a support ticket.
    """
    content: str = Field(..., description="The description of the issue.")
    is_user: bool = Field(..., description="Indicates if the message is from the user (otherwise from support).")


class Ticket(BaseModel):    
    """
    Represents a support ticket with its messages.
    """
    id: str = Field(..., description="A unique identifier for the ticket.")
    name: str = Field(..., description="The name of the person who created the ticket.")
    messages: List[TicketMessage] = Field(..., description="List of messages associated with the ticket.")
    is_open: bool = Field(..., description="If the ticket is still open.")


ticket_generator = llm.with_structured_output(Ticket)
ticket_updater = llm.with_structured_output(TicketMessage)


def create_new_ticket() -> Ticket:
    messages = [
        ("system", TICKET_SYSTEM_PROMPT),
        ("human", GENERATE_NEW_TICKET_PROMPT)
    ]
    return ticket_generator.invoke(messages)


def update_ticket(ticket: dict) -> Ticket:
    ticket_messages = []
    for message in ticket["messages"]:
        message_cls = HumanMessage if message["is_user"] else AIMessage
        ticket_messages.append(message_cls(content=message["content"]))
    prompt = _update_ticket_prompt.invoke({"messages": ticket_messages})
    update = ticket_updater.invoke(prompt)
    ticket["messages"].append(update)
    return Ticket(**ticket)  # unpack the dictionary to create a Ticket object


def read_last_ticket() -> Ticket:

    """
    Reads messages from the ticket that was updated the last.

    Returns:
        Ticket: A `Ticket` object with the ticket id, the name of the user, the status, and the messages.
    """

    open_tickets = [t for t in list(tickets.values()) if t["is_open"]]
    new_ticket = (not open_tickets) or (np.random.rand() < 0.5)
    if new_ticket:
        # generate a new ticket
        ticket = create_new_ticket()
    else:
        # update an existing ticket
        ticket = np.random.choice(open_tickets)
        ticket = update_ticket(ticket)
    return ticket


def send_reply_to_ticket(ticket: Ticket, message: AIMessage, close: bool) -> None:

    """
    Sends a reply to a ticket.

    Args:
        ticket (Ticket): The ticket to reply to.
        message (AIMessage): The message to send as a reply.
        close (bool): If True, the ticket will be closed after the reply.
    """

    ticket.messages.append(TicketMessage(
        content=message.content,
        is_user=False
    ))
    if close:
        ticket.is_open = False

    tickets[ticket.id] = ticket.model_dump()
    with open("./tickets.json", "w") as f:
        json.dump(tickets, f, indent=4)


def rag(query: str) -> List[Document]:

    """
    Retrieve relevant documents.

    Args:
        query (str): The query to retrieve the documents for.

    Returns:
        List[Document]: The retrieved documents.
    """

    pass