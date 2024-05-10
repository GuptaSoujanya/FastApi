from fastapi import FastAPI

app = FastAPI()

fake_database=[{
    "Name" : "soujanya",
    "class" : "Enginnering",
    "working" : "GRT"
},
      {
    "Name" : "sanya",
    "class" : "Ennering",
    "working" : "GT"
},
      {
    "Name" : "s",
    "class" : "E",
    "working" : "GT"
},        
]

@app.get("/")
async def database(a : int = 0 , b: int = 3):
    return fake_database[a : b]

@app.get("/{Item_id}")
async def itemData(Item_id : int | str , q : str |None = None , short : bool = False):
    item = {"Item_id" : Item_id}
    if q:
        item.update({"quarry": q})
    if not short:
        item.update({"discription" : "We all are here to find here"})
    return item
