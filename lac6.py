from fastapi import FastAPI,Path,Query

app = FastAPI()

@app.get("/{list_item}")
async def data(list_item : int = Path(..., gt=10 , le= 20) , q : str | None = None ):
    list_data = {"list_item": list_item}
    if(q is not None):
        list_data.update({"quarrey": q})
    return list_data