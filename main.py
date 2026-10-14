from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field

app = FastAPI(title="Inventory Management API")

class Product(BaseModel):
    name: str = Field(min_length=3)
    category: str = Field(min_length=3)
    price: float = Field(gt=0)
    quantity: int = Field(ge=0)

products = {}

next_id = 1

@app.post("/products",status_code = 201)
def create_product(product: Product):
    global next_id
    product_id = next_id
    products[product_id] = product.model_dump()
    next_id += 1
    return{
        "message": "Product created successfully",
        "product_id": product_id,
        "product_details": products[product_id]
    }

@app.get("/products")
def retrieve_all_products():
    
    return{
        "total_products": len(products),
        "products": products
    }

@app.get("/products/{product_id}")
def retrieve_product_by_id(product_id: int):
    
    if product_id not in products:
        raise HTTPException(
            status_code = 404,
            detail = "Product not found"
        )
    
    return{
        "product_id": product_id,
        "product_details": products[product_id]
    }

@app.put("/products/{product_id}")
def update_product(product_id: int,product: Product):
    
    if product_id not in products:
        raise HTTPException(
            status_code = 404,
            detail = "Product not found"
        )
    products[product_id] = product.model_dump()
    
    return{
        "message": "Product details updated",
        "product_id": product_id,
        "product_details": products[product_id]
    }

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    
    if product_id not in products:
        raise HTTPException(
            status_code = 404,
            detail = "Product not found"
        )
    
    del products[product_id]
    
    return{
        "message": "Product details deleted successfully"
    }

@app.get("/products/filter/category")
def filter_products_by_category(category: str):

    filtered_products = {
        product_id: product
        for product_id, product in products.items()
        if product["category"].lower() == category.lower()
    }

    return {
        "category": category,
        "products": filtered_products
    }

@app.get("/products/filter/price")
def filter_products_by_price(min_price: float = 0, max_price: float = 1000000):

    if min_price > max_price:
        raise HTTPException(
            status_code=400,
            detail="Minimum price cannot be greater than maximum price"
        )

    filtered_products = {
        product_id: product
        for product_id, product in products.items()
        if min_price <= product["price"] <= max_price
    }

    return {
        "products": filtered_products
    }

@app.get("/inventory/low-stock")
def get_low_stock_products(threshold: int = Query(default=5, ge=0)):

    low_stock_products = {
        product_id: product
        for product_id, product in products.items()
        if product["quantity"] < threshold
    }

    return {
        "threshold": threshold,
        "low_stock_products": low_stock_products
    }

@app.get("/inventory/value")
def get_inventory_value():

    total_value = 0
    for product in products.values():
        total_value += product["quantity"] * product["price"]
        
    return {
        "total_inventory_value": total_value
    }