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

class Productupdate(BaseModel):
    name: str | None = None
    description: str | None = None
    price: int | None = None
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
        raise HTTPException(status_code = 404, detail = "Product id not found")
    product = products[product_id]
    return product

@app.get("/product")
async def get_product_by_stock(stock: int | None = None):
    stocks = [i["stock"] for i in products.values()]
    if stock not in stocks:
        raise HTTPException(status_code = 404, detail = "No product has the provided stock")
    product_stock = [product for product in products.values() if product["stock"] == stock ]
    # product_list = []
    # for product in products.values():
    #     if product["stock"] == stock:
    #         product_list.append(product)
    return product_stock

@app.put("/update")
async def update_product(product: Product):
    if product.id not in products.keys():
        raise HTTPException(status_code = 404, detail = "Product ID doesn't exist")
    products[product.id] = {
        "id": product.id,
        "name": product.name,
        "description": product.description,
        "price": product.price,
        "stock": product.stock
    }
    return products[product.id]

@app.patch("/patial_update")
async def partial_update(product_id: int, product_data:Productupdate):
    if product_id not in products.keys():
        raise HTTPException(status_code = 404, detail = "Product ID doesn't exist")
    product = products[product_id]
    if product_data.name is not None:
        product["name"] = product_data.name    
    if product_data.description is not None:
        product["description"] = product_data.description
    if product_data.price is not None:
        product["price"] = product_data.price
    if product_data.stock is not None:
        product["stock"] = product_data.stock
    return product

@app.delete("/delete")
async def delete_product(product_id: int):
    if product_id not in products.keys():
        raise HTTPException(status_code = 404, detail = "Product ID doesn't exist")
    del products[product_id]
    return {"message": "Product deleted successfully"}