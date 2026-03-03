from fastapi import FastAPI
from models import Product
# import uvicorn

# if __name__ == "__main__":
#     uvicorn.run("run:app", host="127.0.0.1", port=8000, reload=True)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/api-endpoint")
async def first_api():
    return {'message': 'Hello Eric!'}

Products = [
    Product(id=1,name="phone1",description="my phone for play game1",quantity=1,price=1345.65),
    Product(id=2,name="phone2",description="my phone for play game2",quantity=2,price=1345.65),
    Product(id=3,name="phone3",description="my phone for play game3",quantity=3,price=1345.65),
    Product(id=4,name="phone4",description="my phone for play game4",quantity=4,price=1345.65),
]

@app.get("/products")
async def read_all_product():
    return Products

@app.get("/product/{id}")
async def read_category_by_query(id: int):
    #products_to_return = []
    for product in Products:
        if product.id == id:
           # products_to_return.append(product)
           return product
    return "Product not found"

# @app.post("/products/create_product")
# async def create_product(new_product=Body()):
#     productS.append(new_product)