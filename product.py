from fastapi import FastAPI, Query, Path, HTTPException
from typing import Annotated
from pydantic import BaseModel


app = FastAPI()

class ProductBase(BaseModel):
    name: str
    description: str
    price: int
    stock: int

class Product(ProductBase):
    id: int

class ProductStock(BaseModel):
    name: str | None = None
    description: str | None = None
    price: str | None = None
    stock: int | None = None

products = {}

@app.get("/")
async def root():
    return {"message": "This is the product API endpoint"}

@app.post("/create", status_code = 201)
async def create_product(product: ProductBase):
    product_id = len(products)
    product_dict = {
        "id": product_id,
        "name": product.name,
        "description": product.description,
        "price": product.price,
        "stock": product.stock
    }
    products[product_id] = product_dict
    return product_dict

@app.get("/products")
async def get_product():
    return products

@app.get("/product/{product_id}")
async def get_product_by_id(product_id: int):
    if product_id not in products.keys():
        raise HTTPException(status_code = 400, detail = "Product id not found")
    product = products[product_id]
    return product

@app.get("/product")
async def get_product_by_stock(stock: int | None = None):
    stocks = [i["stock"] for i in products.values()]
    if stock not in stocks:
        raise HTTPException(status_code = 401, detail = "No product has the provided stock")
    product_stock = [product for product in products.values() if product["stock"] == stock ]
    # product_list = []
    # for product in products.values():
    #     if product["stock"] == stock:
    #         product_list.append(product)
    return product_stock