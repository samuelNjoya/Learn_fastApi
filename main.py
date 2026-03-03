from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List

app = FastAPI(
    title="API Gestion Produits",
    version="1.0.0"
)

class Product(BaseModel):
    name: str = Field(..., example="Smartphone")
    description: str = Field(..., example="Téléphone haute performance")
    price: float = Field(..., gt=0)
    stock: int = Field(..., ge=0)

products_db = []
product_id_counter = 1


@app.post("/products", status_code=status.HTTP_201_CREATED)
def create_product(product: Product):
    global product_id_counter

    new_product = {
        "id": product_id_counter,
        **product.model_dump()
    }

    products_db.append(new_product)
    product_id_counter += 1

    return new_product


@app.get("/products")
def get_products():
    return products_db


@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products_db:
        if product["id"] == product_id:
            return product

    raise HTTPException(status_code=404, detail="Produit non trouvé")


@app.put("/products/{product_id}")
def update_product(product_id: int, updated_product: Product):
    for product in products_db:
        if product["id"] == product_id:
            product.update(updated_product.model_dump())
            return product

    raise HTTPException(status_code=404, detail="Produit non trouvé")


@app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int):
    for product in products_db:
        if product["id"] == product_id:
            products_db.remove(product)
            return

    raise HTTPException(status_code=404, detail="Produit non trouvé")