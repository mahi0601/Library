from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes.books import router as books_router
from backend.routes.authors import router as authors_router

app = FastAPI(
    title="Gutendex API",
    description="API for retrieving books from the Gutenberg database",
    version="1.0.0"
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(books_router, prefix="/books", tags=["Books"])
app.include_router(authors_router, prefix="/authors", tags=["Authors"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Gutendex API"}

