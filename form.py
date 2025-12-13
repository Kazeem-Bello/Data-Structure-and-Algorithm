from fastapi import FastAPI, Path, Query, Form, UploadFile, File
from typing import Annotated, Literal
from pydantic import BaseModel, Field



app = FastAPI()

@app.get("/")
async def root():
    return {"message": "submit yor form below"}

@app.post("/login")
async def form(username: Annotated[str, Form()], 
                 password: Annotated[str, Form(), Query(min_length = 4)]):
    return {"Username": username, 
            "Password": password}

@app.post("/upload")
async def upload(file: Annotated[bytes, File()]):
    return {'file': len(file)}

def save_file(file: UploadFile):
    with open(file.filename, "wb") as f:
        f.write(file.file.read())

@app.post("/uploadfile")
def upload_file(file: UploadFile):
    save_file(file)
    return {"filename": file.filename}
