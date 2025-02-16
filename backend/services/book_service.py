from backend.database import books_collection
from backend.routes.filters import create_filter

async def fetch_books(title, author, language, topic, mime_type, page, page_size):
    query = create_filter(title, author, language, topic, mime_type)
    total_books = await books_collection.count_documents(query)
    books = await books_collection.find(query).sort("download_count", -1).skip((page - 1) * page_size).limit(page_size).to_list(length=page_size)
    return {"total_books": total_books, "books": books}
