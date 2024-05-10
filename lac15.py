from fastapi import FastAPI,status
from pydantic import BaseModel

app = FastAPI()

@app.get("/data/{data_it}" , status_code= status.HTTP_202_ACCEPTED)
async def data_inheret(data_id : str):
    return{"data": data_id}

@app.put("/data/work" , status_code=201)
async def data_background():
    return{"work": "work"}