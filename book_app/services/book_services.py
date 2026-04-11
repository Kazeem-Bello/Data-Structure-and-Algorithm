from book_app.schema.book_schema import BookCreate, Book
from book_app.database. book_db import books

class BookServices:
    @staticmethod
    def create_book(book_in: BookCreate):
        book_info: dict = book_in.model_dump()
        book_id = str(len(books) + 1)
        new_book = Book(id = book_id,
                    **book_info)
        books[book_id] = new_book
        return new_book
    
    @staticmethod
    def get_book():
        return books
    
    @staticmethod
    def get_book_id(id: str):
        for book_id in books.keys():
            if id == book_id:
                return books[id]

