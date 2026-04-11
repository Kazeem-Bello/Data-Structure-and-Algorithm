from pydantic import BaseModel

class BookBase(BaseModel):
    author: str
    title: str
    publish_year: int
    price: int


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: str


