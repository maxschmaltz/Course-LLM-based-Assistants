from langchain_core.messages import AIMessage
from langchain_core.documents import Document
from typing import List


class AdaptiveRAGAgent:

    def __init__(self, **kwargs):
        
        """
        Initialize the AdaptiveRAGAgent. It should also load
        the index from the `knowledge/` folder here.
        """

        self.llm = ...
        pass

    def classify(self, query: str) -> str:
        
        """
        Classify the question and return the destination.
        
        Args:
            query (str): The question to answer
            
        Returns:
            str: The further processing destination (direct, simple RAG, iterative RAG)
        """

        pass

    def rerank(self, docs: List[Document]) -> List[Document]:

        """
        Rerank the documents with the LLM to improve the search results.
        
        Args:
            docs (List[Document]): The list of retrieved documents
            
        Returns:
            List[Document]: The reranked list of documents
        """

        pass

    def answer_directly(self, query: str) -> AIMessage:
        
        """
        Answer the question directly without using the index.
        
        Args:
            query (str): The question to answer
            
        Returns:
            AIMessage: The LLM response to the question
        """

        pass

    def simple_rag(self, query: str) -> AIMessage:
        
        """
        Answer the question in the one-step RAG manner.
        
        Args:
            query (str): The question to answer
            
        Returns:
            AIMessage: The LLM response to the question
        """

        pass

    def iterative_rag(self, query: str) -> AIMessage:
        
        """
        Answer the question in the iterative RAG manner.
        
        Args:
            query (str): The question to answer
            
        Returns:
            AIMessage: The LLM response to the question
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


def init_rag_agent(**kwargs) -> AdaptiveRAGAgent:
    
    """
    Initialize the AdaptiveRAGAgent.
    
    Args:
        **kwargs: Additional keyword arguments for initialization
        
    Returns:
        AdaptiveRAGAgent: The initialized agent
    """

    return AdaptiveRAGAgent(**kwargs)