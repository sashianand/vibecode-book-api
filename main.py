from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List

app = FastAPI(
    title="VibeCode Book API",
    description="An API for managing a collection of books and their reviews.",
    version="1.0.0",
)

# Allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Models ---

class Review(BaseModel):
    rating: int = Field(..., ge=1, le=5, description="Rating from 1 to 5")
    comment: str

class Book(BaseModel):
    id: int
    title: str
    author: str
    genre: str
    reviews: List[Review] = []

class BookCreate(BaseModel):
    title: str
    author: str
    genre: str

# --- In-memory database ---

books_db: List[Book] = [
    Book(id=1, title="The Great Gatsby", author="F. Scott Fitzgerald", genre="Classic", reviews=[Review(rating=5, comment="A masterpiece!")]),
    Book(id=2, title="To Kill a Mockingbird", author="Harper Lee", genre="Classic", reviews=[]),
]
next_book_id = 3

# --- Endpoints ---

@app.get("/books", response_model=List[Book], summary="Get all books")
async def get_books():
    """
    Retrieve a list of all books in the library.
    """
    return books_db

@app.post("/books", response_model=Book, status_code=201, summary="Add a new book")
async def add_book(book_create: BookCreate):
    """
    Add a new book to the library. The book ID is generated automatically.
    """
    global next_book_id
    new_book = Book(
        id=next_book_id,
        **book_create.dict(),
        reviews=[]
    )
    books_db.append(new_book)
    next_book_id += 1
    return new_book

@app.post("/books/{book_id}/reviews", response_model=Book, summary="Add a review to a book")
async def add_review_to_book(book_id: int, review: Review):
    """
    Add a review to a specific book by its ID.
    """
    for book in books_db:
        if book.id == book_id:
            book.reviews.append(review)
            return book
    raise HTTPException(status_code=404, detail="Book not found")

# Vercel handler
from mangum import Mangum
handler = Mangum(app) 