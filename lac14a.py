from fastapi import FastAPI 
from pydantic import BaseModel , EmailStr

app = FastAPI()

class userDetails(BaseModel):
    name :  str
    email : EmailStr
    Phone : str | None = None
    
class useCredentials(userDetails):
    User_name : str
    password : str
    
class useProtectredPassword(userDetails):
    Protected_password : str
    
class useDataOut(userDetails):
    pass
    
def fake_password_genrater(use_new_password : str):
    return f"supersecured{use_new_password}"

def fake_save_password(user_data : useCredentials):
    hashed_password = fake_password_genrater(user_data.password)
    print(hashed_password)
    user_in_DB = useProtectredPassword(**user_data.dict() , Protected_password=hashed_password)
    print("user pasword saved")
    return user_in_DB

@app.post("/user/", response_model=useDataOut)
def creat_new_user(user_in : useCredentials):
    user_server = fake_save_password(user_in)
    return user_server


    
