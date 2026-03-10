from fastapi import FastAPI, HTTPException, status
from database import SessionLocal, engine
from typing import List
from models import Product
import db_models

app = FastAPI(title="API Gestion Produits", version="1.0.0")

db_models.Base.metadata.create_all(bind=engine)  # Crée les tables dans la DB

products_db = [
      Product(name="Smartphone", description="Téléphone haute performance", price=699.99, stock=50),
      Product(name="Laptop", description="Ordinateur portable puissant", price=1299.99, stock=30),
      Product(name="Headphones", description="Casque audio de qualité", price=199.99, stock=100),
]
product_id_counter = 1

@app.get("/")
def read_root():
    return {"message": "Hello World this is my first API with FastAPI"}

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

def init_db():
    db = SessionLocal()
    count = db.query(db_models.Product).count()
    if count == 0:
        for product in products_db:
            # db_product = db_models.Product(
            #     name=product.name,
            #     description=product.description,
            #     price=product.price,
            #     stock=product.stock
            # )
            db_product = db_models.Product(**product.model_dump())
            db.add(db_product)
 
        db.commit()

init_db()

@app.get("/products")
def get_products():
    # db = SessionLocal()
    # db.query()
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