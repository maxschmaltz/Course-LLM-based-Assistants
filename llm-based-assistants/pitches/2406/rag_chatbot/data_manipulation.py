from langchain_core.documents import Document
from typing import List


def load_data(folder_path: str) -> List[Document]:
    
    """
    Load data from the files of a folder.
    
    Args:
        folder_path (str): The path to the data folder
        
    Returns:
        List[Document]: A list of `Document` entries
    """

    pass


def split_data(documents: List[Document]) -> List[Document]:
    
    """
    Split documents into smaller chunks.
    
    Args:
        documents (List[Document]): The list of documents to split
        
    Returns:
        List[Document]: A list of `Document` entries, each representing a chunk
    """

    pass


def create_index(documents: List[Document]) -> None:
    
    """
    Create an index for the documents. Should store the index in a persistent storage
    in the `knowledge` folder.
    
    Args:
        documents (List[Document]): The list of documents to index
    """

    pass


def init_index():

    """
    Main function to execute the data manipulation tasks.
    """

    data_path = "./resources/"
    
    # load data
    documents = load_data(data_path)
    # split data into chunks
    chunks = split_data(documents)
    # create index for the chunks
    create_index(chunks)