from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def root():
    file = open("index.html", "r")

    return HTMLResponse(content=file.read(), status_code=200)
