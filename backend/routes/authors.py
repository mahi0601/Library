from fastapi import APIRouter
from backend.database import authors_collection

router = APIRouter()

@router.get("/authors")
async def get_authors():
    authors = await authors_collection.find().to_list(length=100)
    return {"authors": authors}
