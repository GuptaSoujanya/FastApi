from fastapi import FastAPI,Path , Query ,Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class student(BaseModel):
    Fname: str
    Lname : str|None
    marks : int
    per : float |None

class users(BaseModel):
    ID : str
    Salary: int

@app.put("/{put_data}")
async def app_data(*,put_data : int = Path(..., gt=0,lt= 100),
                   q : Optional[str] = None,
                   main_data: str = Query(None, max_length=20),
                   student_data: student | None = None,
                   user_data : users = Body(..., embed=True),
                   importanat : int = Body(...)):
    item = {"id": put_data}
    if q:
        item.update({"quarry": q})
    if main_data:
        item.update({"marks": main_data})
    if student_data:
        item.update({"item": student_data})
    if user_data:
        item.update({"user_data": user_data})
    if importanat:
        item.update({"important" : importanat})
    return item