from fastapi import FastAPI,Query

app = FastAPI()

@app.get("/{List_id}")
async def list_data(List_id: str,q : list[str]= Query(None,max_length=10,description="Heyy I am default value")):
    return{"List_id":List_id,"quarry" : q}