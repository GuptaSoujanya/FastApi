from fastapi import FastAPI
from pydantic import BaseModel , SecretStr
from typing import Literal
app = FastAPI()

class BasicDeatils(BaseModel):
    name : str
    Stream :str
    discription : str | None=None
    
class AdvanceDetails(BasicDeatils):
    password : SecretStr
    
class FetchDetails(AdvanceDetails):
    pass

@app.post("/data/{id}")
def data_new_update(ids : int | str, new_data :FetchDetails | None = None):
    items = {"id": ids, "data":new_data}
    return items


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 10.5
    tags: list[str] = []

items = {
    "frist": {"name": "Foo", "price": 50.2},
    "saecond": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "third": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}
       
@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
def data_include(item_id : Literal["frist" ,"saecond" ,"third"]):
    return items[item_id]

