from fastapi import FastAPI , File , UploadFile
from starlette.responses import HTMLResponse

app = FastAPI()

@app.post("/new_data")
async def file_upload(files_upload : list[bytes] = File(...)):
    return {"file_len" : [len(Files) for Files in files_upload]}

@app.post("/upload_file")
async def file_upload(files : list[UploadFile] = File(...)):
    return{"file_len": [file.filename for file in files]}

@app.get("/")
async def main():
    with open("./form.html", "r") as file:
        contant = file.read()
    return HTMLResponse(content=contant)