import json
from langchain_core.tools import tool

# load KG from a JSON file
with open("./kg.json", "r") as f:
    KG = json.load(f)


def overlap(keyword: str, target: str) -> bool:

    """
    Check if the keyword overlaps with the target string.
    
    Args:
        keyword (str): The keyword to check
        target (str): The target string to check against
        
    Returns:
        bool: True if there is an overlap, False otherwise
    """
    
    return keyword.lower() in target.lower() or any(word in keyword.lower() for word in target.lower().split())


@tool
def query_knowledge_graph(keywords: list) -> dict:

    """
    Query the linguistics knowledge graph for information.
    
    Args:
        keywords (List[str]): The query keywords
        
    Returns:
        Dict[str, Any]: Query results with relevant information:
        * entities: List of entities related to the keywords
        * relations: List of relations related to the keywords
    """

    pass