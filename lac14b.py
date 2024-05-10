from fastapi import FastAPI
from pydantic import BaseModel, Field, HttpUrl, EmailStr
from typing import Union,Literal

app = FastAPI()

class BaseItem(BaseModel):
    description: str
    type_sandy: str |None =None


class CarItem(BaseItem):
    type_sandy : str = "car"


class PlaneItem(BaseItem):
    type_sandy : str = "car"
    size: int


items = {
    "item1": {"description": "All my friends drive a low rider", "type_sandy": "car"},
    "item2": {
        "description": "Music is my aeroplane, it's my aeroplane",
        "type_sandy": "plane",
        "size": 5,
    },
}


@app.get("/items/{item_id}", response_model=Union[PlaneItem, CarItem])
async def read_item(item_id: Literal["item1", "item2"]):
    return items[item_id]