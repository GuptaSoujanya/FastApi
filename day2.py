from fastapi import FastAPI
from enum import Enum

app = FastAPI()

@app.get("/")
async def root_fuc():
    return{"name" : "sandy"}

class obj(str , Enum):
    fruite = "apple"
    vegitable = "brockly"
    dairy = "colclates"

@app.get("/{obj_items}")
def item_list(obj_items: obj | str):
    if obj_items == obj.fruite:
        return{"food name": obj_items , "message":"you are on fruits"}
    elif obj_items == obj.vegitable:
        return{"food name": obj_items , "message" : "you are on diffrent level"}
    else :
        return{"message" : "try again"}