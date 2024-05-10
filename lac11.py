from fastapi import FastAPI , Path , Query , Cookie , Header , Body

app = FastAPI()

@app.get("/item/{cokiee_ids}")
async def data_get_method(
    cokiee_id : str | None = Cookie(None),
    accept_encoding : str | None = Header(None),
    sec_ch_ua: str | None = Header(None),
    host: str | None = Header(None)
):
    item = {"cokiee":cokiee_id, "Accept-Encoding" : accept_encoding , "Sec-Ch-Ua" : sec_ch_ua, "host" : host}
    return item