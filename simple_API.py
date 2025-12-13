from fastapi import FastAPI, Form, Query, Path
from typing import Annotated, Literal
from pydantic import BaseModel, Field

app = FastAPI()

book = {}

book_1 = {"author": "Adewale", "year": 1996, "country": "nigeria", "language": "yoruba"}


@app.get("/")
def root():
    return {"message": "welcome to my first API"}

@app.get("/item/{item_id}") #with path parameter
def read_item(item_id: Annotated [int, Path(min_length = 2)]):
    return {"item_id": item_id}


@app.get("/read")
def read_q(q: Annotated[ str | None, Query(max_length = 50)] = None):
    result = {"Item": ["banana", "apple"]}
    if q:
        result["Query"] = q
    return result


@app.get("/query")
async def query(q: Annotated[ list[str], Query(min_length = 3)]):
    query_item = {"q": q}
    return query_item

@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get")],
    q: Annotated[str | None, Query(alias="item-query")] = None
):
    results = {"item_id": item_id}
    if q:
        results["q"] = q
    return results

class FilterParams(BaseModel):
    model_config = {"extra": "forbid"}

    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []


@app.get("/filter/")
async def read_filter(filter_query: Annotated[FilterParams, Query()]):
    return filter_query

# @app.post("/form")
# async def form(name : Annotated[str | form()])


