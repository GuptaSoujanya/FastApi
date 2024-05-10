from fastapi import FastAPI,Body , Path , Query
from pydantic import BaseModel , Field
from typing import Optional

app = FastAPI()

class Image(BaseModel):
    length : int
    black_and_white : bool = Field (True)
    hiegth : int
    
class data_set(BaseModel):
    eid : int
    fname : str
    lname : str
    salary : Optional[str] = None
    tex : int | None
    Location : str  = Field ("Indore" , description="Enter employ location here")
    Images : Image | None
    

@app.put("/data/{item_id}")
def loacat_data(item_id : int = Path(gt=0 , lt= 100), 
                q : Optional[str] = Query(None , max_length=20),
                data : Optional[data_set] = None):
    items = {"item_id": item_id , "data" : data}
    if q:
        items.update({"quarry" : q})
    return items

@app.post("/data/new/{offer_id}")
def upload_data(offer_id: int , Image_data : Image):
    item_data={"id":offer_id , "Image_data" : Image_data}
    return item_data

@app.post("/data/one")
async def creat_non(blash: dict[int , float ]):
    return blash
