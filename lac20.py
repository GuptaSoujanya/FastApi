from fastapi import FastAPI,status
from enum import Enum
from pydantic import BaseModel
app = FastAPI()

class data(BaseModel):
    name:str
    company : str
    
class item(Enum):
    user:"user"
    user2:"user2"


@app.get("/data",
         response_model= data,
         tags=["data"],
         status_code=status.HTTP_202_ACCEPTED
         )
def data_function(items:data):
    """
    - **Name**: Soujanya Gupta
    - **Comapant**: GRT
    - **Domain**: Backend
    """
    return items

@app.get("data",
         tags=[item.user])
def data_in_take(item:str):
    return {"data":"sandy"}