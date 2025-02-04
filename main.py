from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str

@app.get("/")
def read_root():
    return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

@app.get("/teste/")
def read_item():
    return {"eba"}

# http://127.0.0.1:8000/items/1?filter=null&page=0
@app.get("/items/{item_id}")
def read_item(item_id: int, page: int, item: Item, filter: str | None = None):
    return {"QUALQUER COISA": item_id, "FILTER": filter}

