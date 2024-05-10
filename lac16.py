from fastapi import FastAPI,Form , Body
from pydantic import SecretStr
app = FastAPI()

@app.post("/login")
def form_data(username: str = Form(...) ,
              password: SecretStr= Form(...)
               ):
    return{"username": username , "password": password}

@app.post("/login/data")
def form_data(username: str = Body(...) , password: SecretStr= Body(...)):
    return{"username": username , "password": password}