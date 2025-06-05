from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional,List

# class Item(BaseModel):
#     itemid: int
#     description: str
#     owner: Optional[str] = None

class Owner(BaseModel):
    name: str
    address: str

class Item(BaseModel):
    itemid: int
    description: str
    owner: Optional[Owner] = None
    ratings: List[float]
    available: bool

api = FastAPI()

@api.post('/item')
def post_item(item: Item):
    return item
# -i "Affiche aussi les en-têtes de la réponse HTTP."

# curl -X 'POST' -i \
#   'http://127.0.0.1:8000/item' \
#   -H 'Content-Type: application/json' \
#   -d '{
#   "itemid": 1234,
#   "description": "my object",
#   "owner": "Daniel"
# }'