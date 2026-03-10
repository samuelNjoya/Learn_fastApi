from pydantic import BaseModel, Field

class Product(BaseModel):
    name: str = Field(..., example="Smartphone")
    description: str = Field(..., example="Téléphone haute performance")
    price: float = Field(..., gt=0)
    stock: int = Field(..., ge=0)