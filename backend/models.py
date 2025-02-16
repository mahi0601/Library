from pydantic import BaseModel, Field
from typing import List, Optional

class FormatModel(BaseModel):
    mime_type: str
    link: str

class BookModel(BaseModel):
    id: str = Field(..., alias="_id")
    title: str
    authors: List[str]
    genres: List[str] = []
    languages: List[str]
    subjects: List[str] = []
    bookshelves: List[str] = []
    download_count: int
    formats: List[FormatModel]

class BookResponseModel(BaseModel):
    total_books: int
    books: List[BookModel]

class AuthorModel(BaseModel):
    id: str = Field(..., alias="_id")
    name: str

class SubjectModel(BaseModel):
    id: str = Field(..., alias="_id")
    name: str

class BookshelfModel(BaseModel):
    id: str = Field(..., alias="_id")
    name: str

class LanguageModel(BaseModel):
    id: str = Field(..., alias="_id")
    code: str
    name: str
