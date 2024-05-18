from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel


app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.get("/", response_class=HTMLResponse)
async def root():
    file = open("index.html", "r")

    return HTMLResponse(content=file.read(), status_code=200)

@app.post("/")
async def readItem(item: Item):
    print(item.dict())
    return item