from fastapi import FastAPI,HTTPException, Request , status
from fastapi.responses import JSONResponse,PlainTextResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as starlatteHTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from fastapi.exception_handlers import request_validation_exception_handler , http_exception_handler

app = FastAPI()

items = {
    "s" : "woking poperly"
}

@app.get("/data/{fake_type}")
def data_in_working(fake_type :str):
    if fake_type not in items:
        raise HTTPException(status_code=404 , 
                            detail="this elemet is not in list",
                            headers={"experiment_headers": "data could not loaded"}
                            )
    return{"id":items[fake_type]}

# BY using class and genrate owns exepetion type

class defaultExeption(Exception):
    def __init__(self , name):
        self.name = name
    
    
@app.exception_handler(defaultExeption)
async def check_validation(req : Request , ece : defaultExeption):
    return JSONResponse(
        status_code=404,
        headers={"data-x":"onle for testing perpose"},
        content = {"message" : f"oops Data is not valid !!!!{ece.name}"}
    )
    
@app.get("/data_exepetion/{id_works}")
async def main(id_works : str):
    if id_works != "data":
        raise defaultExeption(name=id_works)
    return{"id":id_works}


# @app.exception_handler(RequestValidationError)
# async def request_validation_error(request,exc):
#     return PlainTextResponse(
#         str(exc),
#         status_code=409
#     ) 
    
# @app.get("/data/from/{route_id}")
# async def request_data_check(route_id : str):
#     if route_id == "3":
#         raise HTTPException(status_code= 404, 
#                       detail="data is not valid")
#     return {"route_id" : route_id}

# @app.exception_handler(starlatteHTTPException)
# async def request_starlaate_exeption(request , exc):
#     return PlainTextResponse(
#         str(exc.detail),
#         status_code= exc.status_code
#     )

# @app.exception_handler(RequestValidationError)
# async def validation_eception_handller(request : Request , exc : RequestValidationError):
#     return JSONResponse(
#         status_code= status.HTTP_422_UNPROCESSABLE_ENTITY,
#         content=jsonable_encoder({"details":exc.errors(),"blahblahh":exc.body})
#     )
    
# class items(BaseModel):
#     title : str
#     size : int
    
# @app.post("/items")
# async def create_items(item:items):
#     return item

@app.exception_handler(RequestValidationError)
async def data_heandle(request,exc):
    print(f"OMG! The Client sent validation data!:{exc}")
    return await request_validation_exception_handler(request ,exc)

@app.exception_handler(starlatteHTTPException)
async def data_load_worker(request,exc):
    print(f"error pass from :{exc}")
    return await http_exception_handler(request , exc)

@app.get("/data/load/on/{link}")
async def data_working(link : str):
    if(link == "3"):
        raise HTTPException(status_code=418 , detail={"hyy yoy are in "})
    return{"id":link}