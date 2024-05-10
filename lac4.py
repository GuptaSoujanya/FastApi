from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class data(BaseModel):
    name: str
    company_name : str
    salary: int
    nationality : str | None =None
    working : Optional[bool] = None

@app.put("/{User_data}")
async def data_display(data: data):
    old_data = data.dict()
    if data.nationality == "Indian":
        old_data.update({"Discription" : "Jai hind"})
    elif data.nationality == None:
        old_data.update({"Discription" : "Warning!!! you should enter the nationality"})
    else:
        old_data.update({"Discription": "You are for outside"})
    return old_data

@app.put("/{User_data}/{user_id}")
async def Create_new_put_request(user_id : int , data: data,q: Optional[str]=None ):
    result = {"Id": user_id , **data.dict()}
    if q:
        result.update({"quarry" :q})
    return result