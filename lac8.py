from fastapi import FastAPI, Path, Query , Body
from pydantic import Field , BaseModel
from typing import Optional

app = FastAPI()

class post_data(BaseModel):
    fname : str
    lname : str | None = Field("API testing Sucessfually")

@app.put("/data/{new_data}")
async def new_function(new_data : int = Path(...,gt=0,lt=100),
                       q : Optional[str] = None,
                       post_d: post_data |None = None):
    data = {"id": new_data}
    if q:
        data.update({"qaurry": q})
    if post_d:
        data.update({"post_data":post_d})
    return data