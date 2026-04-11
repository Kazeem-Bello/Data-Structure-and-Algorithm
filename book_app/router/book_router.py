from fastapi import APIRouter, status, HTTPException
from book_app.schema.book_schema import BookCreate
from book_app.services.book_services import BookServices


router = APIRouter()

# create book
@router.post("/", status_code = status.HTTP_201_CREATED)
async def creat_book(book_in: BookCreate):
    new_book = BookServices.create_book(book_in)
    return {"message": "success", "data": new_book}


# get all books
@router.get("/", status_code = 200)
async def get_books():
    book = BookServices.get_book()
    return book

# get book with id
@router.get("/{id}", status_code = 200)
async def get_books_id(id: str):
    book = BookServices.get_book_id(id)
    if not book:
        raise HTTPException( status_code = 404, detail = "ID not found")
    return book

# update book

# delete book