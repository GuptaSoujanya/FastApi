from fastapi import FastAPI,Form ,UploadFile , Body,File

app = FastAPI()

@app.post("/files/")
async def data_experiment(
    file : bytes = File(...,de),
    uploaod_file : UploadFile = File(...),
    token : str = Form(None),
    hello : str = Body(None)
):
    
    return{
        "file" : len(file) ,
        "uploaod_file" :uploaod_file.content_type,
        "token" : token,
        "hello" : hello
    }