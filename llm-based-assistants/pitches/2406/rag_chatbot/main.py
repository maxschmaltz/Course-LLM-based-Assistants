from rag_chatbot.data_manipulation import init_index
from rag_chatbot.agent import init_rag_agent


def init_pipeline(**kwargs):
    # initialize the index, this creates an index in the "knowledge/" directory
    init_index()
    # initialize the RAG agent with the index, this load the index into the agent
    rag_agent = init_rag_agent(**kwargs) # put yor parameters here
    return rag_agent