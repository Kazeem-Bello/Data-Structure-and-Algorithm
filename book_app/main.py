from fastapi import FastAPI
from book_app.router.book_router import router as book_router

app = FastAPI()

app.include_router(book_router, prefix = "/book", tags = ["Book"])


# @app.get("/")
# async def root():
#     return {"message": "Bigger Apps"}