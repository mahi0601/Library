from backend.database import authors_collection
from fastapi import HTTPException
from typing import List, Optional


async def fetch_authors(limit: int = 100) -> List[dict]:
    """
    Fetch a list of authors from the database.
    
    Args:
        limit (int): Number of authors to retrieve (default: 100)
    
    Returns:
        List[dict]: A list of author objects.
    """
    authors = await authors_collection.find().limit(limit).to_list(length=limit)
    return authors


async def fetch_author_by_name(author_name: str) -> dict:
    """
    Fetch a single author by their name.
    
    Args:
        author_name (str): The name of the author.
    
    Returns:
        dict: Author object if found.
    
    Raises:
        HTTPException: If the author is not found.
    """
    author = await authors_collection.find_one({"name": {"$regex": f"^{author_name}$", "$options": "i"}})
    if author:
        return author
    raise HTTPException(status_code=404, detail="Author not found")


async def search_authors_by_partial_name(search_term: str, limit: int = 10) -> List[dict]:
    """
    Search for authors using a partial name match (case-insensitive).
    
    Args:
        search_term (str): Partial name search term.
        limit (int): Number of authors to retrieve (default: 10).
    
    Returns:
        List[dict]: A list of matching authors.
    """
    authors = await authors_collection.find(
        {"name": {"$regex": search_term, "$options": "i"}}
    ).limit(limit).to_list(length=limit)

    return authors
