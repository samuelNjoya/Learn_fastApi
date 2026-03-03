from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List

app = FastAPI(
    title="API Gestion Produits",
    description="API professionnelle pour gérer un catalogue de produits",
    version="1.0.0"
)

# ==========================
# SCHEMAS (Pydantic)
# ==========================

class ProductBase(BaseModel):
    name: str = Field(..., example="Smartphone")
    description: str = Field(..., example="Téléphone haute performance")
    price: float = Field(..., gt=0, example=499.99)
    stock: int = Field(..., ge=0, example=10)


class ProductCreate(ProductBase):
    pass


class ProductResponse(ProductBase):
    id: int

    class Config:
        from_attributes = True


# ==========================
# FAKE DATABASE (liste mémoire)
# ==========================

products_db = []
product_id_counter = 1


# ==========================
# ROUTES
# ==========================

@app.post(
    "/products",
    response_model=ProductResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Produits"],
    summary="Créer un produit"
)
def create_product(product: ProductCreate):
    global product_id_counter

    new_product = {
        "id": product_id_counter,
        **product.model_dump()
    }

    products_db.append(new_product)
    product_id_counter += 1

    return new_product


@app.get(
    "/products",
    response_model=List[ProductResponse],
    tags=["Produits"],
    summary="Lister tous les produits"
)
def get_products():
    return products_db


@app.get(
    "/products/{product_id}",
    response_model=ProductResponse,
    tags=["Produits"],
    summary="Obtenir un produit par ID"
)
def get_product(product_id: int):
    for product in products_db:
        if product["id"] == product_id:
            return product

    raise HTTPException(
        status_code=404,
        detail="Produit non trouvé"
    )


@app.delete(
    "/products/{product_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Produits"],
    summary="Supprimer un produit"
)
def delete_product(product_id: int):
    for product in products_db:
        if product["id"] == product_id:
            products_db.remove(product)
            return

    raise HTTPException(
        status_code=404,
        detail="Produit non trouvé"
    )