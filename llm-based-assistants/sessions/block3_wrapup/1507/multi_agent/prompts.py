from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


TICKET_SYSTEM_PROMPT = """\
Imagine there is an app called FitTrack Pro: a comprehensive fitness tracking mobile \
app that helps you monitor your workouts, track your progress, set fitness goals, \
and maintain a healthy lifestyle. The app combines exercise tracking, nutrition logging, \
sleep monitoring, and social features to provide a complete wellness experience.

Your task is to be a bit creative and generate support tickets to train \
the support system of FitTrack Pro.
"""


GENERATE_NEW_TICKET_PROMPT = """\
You are about to generate a new support ticket for the FitTrack Pro app. \
Please generate the following details:
1. A unique ticket ID.
2. The name of the user who created the ticket.
3. A single message from the user with the description of the issue the user is facing.
4. It should be still open.

Make it concise and relevant to the app's description.
"""


UPDATE_TICKET_PROMPT = """\
You are now given a message history for an existing support ticket. \
Please generate a new user message to update the ticket with the following details:
1. Content: the description of the human answer to the previous message given the history.
2. It is a user message.

Make it concise and relevant to ticket history.
"""


_update_ticket_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", TICKET_SYSTEM_PROMPT),
        ("human", UPDATE_TICKET_PROMPT),
        MessagesPlaceholder(variable_name="messages")
    ]
)