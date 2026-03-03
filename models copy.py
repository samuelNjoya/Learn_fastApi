from pydantic import BaseModel

# suppression de __ini__ car pydantic gère déja ça et lors de l"appel de la class specifier avec les noms
class Product(BaseModel):
    id:int
    name:str
    description:str
    quantity:int
    price:float



    