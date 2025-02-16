from fastapi import APIRouter, Query, HTTPException
from typing import List, Optional
from backend.database import books_collection
from backend.models import BookModel, BookResponseModel

router = APIRouter()

@router.get("/books", response_model=BookResponseModel)
async def get_books(
    title: Optional[str] = None,
    author: Optional[str] = None,
    language: Optional[List[str]] = Query(None),
    topic: Optional[str] = None,
    mime_type: Optional[str] = None,
    page: int = 1,
    page_size: int = 25
):
    query = {}

    if title:
        query["title"] = {"$regex": title, "$options": "i"}
    if author:
        query["authors"] = {"$regex": author, "$options": "i"}
    if language:
        query["languages"] = {"$in": language}
    if topic:
        query["$or"] = [
            {"subjects": {"$regex": topic, "$options": "i"}},
            {"bookshelves": {"$regex": topic, "$options": "i"}}
        ]
    if mime_type:
        query["formats.mime_type"] = mime_type

    total_books = await books_collection.count_documents(query)
    books = await books_collection.find(query).sort("download_count", -1).skip((page - 1) * page_size).limit(page_size).to_list(length=page_size)

    return {"total_books": total_books, "books": books}

@router.get("/books/{book_id}", response_model=BookModel)
async def get_book(book_id: str):
    book = await books_collection.find_one({"_id": book_id})
    if book:
        return book
    raise HTTPException(status_code=404, detail="Book not found")
