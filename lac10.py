from fastapi import FastAPI , Body , Path , Query
from pydantic import BaseModel , Field

app = FastAPI()

class default_data(BaseModel):
    fname : str 
    lname : str 
    age: int 
    salary : int | None = None
    
    # class Config:
    #     schema_extra = {
    #         "example" :{
    #             "fname" :"Soujanya",
    #             "lname" : "Gupta",
    #             "age" : 21,
    #             "salary" : 230000,
    #         }
    #     }
        
        
@app.put("/data/{serever_id}")
async def data_put_server(server_id : int ,
                data : default_data = Body(... , 
                    examples={
                        "Normal":{
                            "summary":"this is frist type",
                            "discription":"heyy this is discription",
                            "values":{
                                "fname" :"Soujanya",
                                "lname" : "Gupta",
                                "age" : 21,
                                "salary" : 230000,
                            }
                        },
                        "Working":{
                            "summary":"this is seconnd",
                            "discription":"heyy this is discription of work",
                            "values":{
                                "fname" :"Sandy",
                                "lname" : "hyy",
                                "age" : 61,
                                "salary" : 200030000,
                            }
                        }
                    })):
    item = {"id": server_id , "data" : data}
    return item