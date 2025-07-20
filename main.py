from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()
products = []

class Product(BaseModel):
    id:int
    name:str
    price:float 
    description: Optional[str] = None

@app.get("/")
def main():
    return {"message":"Hello World"}

@app.post("/product")
def create_product(product:Product):
    products.append(product)
    return product

@app.get("/product")
def get_products():
    return products

@app.get("/product/{id}")
def get_product(id:int):
    for product in products:
        if product['id'] == id:
            return product
    return {"message": "Product not found"}

@app.put("/product/{id}")
def update_product(id:int,product:Product):
    for index,p in enumerate(product):
        if p.id == id:
            products[index] = product 
            return product 
    return {"message":"Product not found"}

@app.delete("/product/{id}")
def delete_product(id:int):
    for index,p in enumerate(products):
        if p.id == id:
            del products[index]
            return {"message":"Product deleted"}
    return {"message":"Product not found"}