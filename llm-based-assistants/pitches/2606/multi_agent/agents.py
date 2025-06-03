from langchain_core.messages import AIMessage
from typing import Tuple, Union

from multi_agent.tools import read_last_ticket, send_reply_to_ticket, rag


class SupportLaMA:

    def __init__(self, **kwargs):
        
        """
        Initialize the SupportLaMA. It should also initialized all the agents.
        """

        self.llm = ...
        self.ticket_manager = ...
        self.classifier = ...
        self.support_expert = ...
        pass

    def ticket_manager_node(self, query_or_answer: Union[str, AIMessage]) -> AIMessage:
        
        """
        Get the ticket manager to call the `read_last_ticket` tool
        and formulate the query based on the previous ticket messages and the last message
        if the pipeline is started with a new ticket message.
        Otherwise, if it is called by the support expert, it should generate
        a personalized answer and use the `send_reply_to_ticket` tool to
        reply to the ticket. Note that in this case, it should also
        decide whether to close the ticket or not. 

        Args:
            query_or_answer (str or AIMessage): The ask to get the last ticket message
            or the answer send back from the support expert to reply to the ticket
        
        Returns:
            AIMessage: The query based on the ticket message history
        """

        pass

    def classify(self, query: str) -> AIMessage:
        
        """
        Classify the query and return the label: green (unimportant), yellow (intermediate), or red (urgent)
        
        Args:
            query (str): The question to answer
            
        Returns:
            str: The label
        """

        pass

    def support_expert_node(self, query: str, label: str) -> Tuple[str, AIMessage]:

        """
        Get the support expert agent to handle the workflow based on the label:
            * If the label is green (unimportant), it retrieves the answer to this query itself (use the RAG tool)
            * If the label is yellow (intermediate), it self-reflects if it can answer it itself
            (them the green scenario applies) or not (then the red scenario applies)
            * If the label is red (urgent), the _support expert_ should interrupt the workflow to
            receive the input from the human expert; it then formulates
            the question for the human and generates its output based on the human input
        
        Args:
            query (str): The question to answer
            label (str): The importance label of the query
            
        Returns:
            str: next destination (back to the ticket manager, ask the human expert, or to the decision node)
            AIMessage: The corresponding AI message: answer if returning to the ticket manager,
            question for the human expert if returning to the human expert, or none if the decision node is chosen
        """

        pass

    def human_intervention_required(self, query: AIMessage) -> bool:

        """
        Decide if the human intervention is required based on the query.
        
        Args:
            query (str): The question to decide on
            (you need to retrieve the content from the AIMessage)
            
        Returns:
            bool: True if human intervention is required, False otherwise
        """

        pass

    def ask_human_expert(self, query: AIMessage) -> AIMessage:

        """
        Interrupt the workflow and ask the human expert for help with the query.
        
        Args:
            query (AIMessage): The question to ask the human expert
            (you need to retrieve the content from the AIMessage)
            
        Returns:
            AIMessage: The answer of the human expert (wrap it in AIMessage)
        """

        pass

    def run(self, query: str) -> AIMessage:

        """
        Run the agent with the given query.
        
        Args:
            query (str): The question to answer
            
        Returns:
            AIMessage: The LLM response to the question
        """

        pass