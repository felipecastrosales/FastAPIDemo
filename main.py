from typing import Union

from fastapi import FastAPI
from fastapi.params import Query
from pydantic import BaseModel, Field
from typing_extensions import Annotated

app = FastAPI(
    title="Totem de Vendas",
)

class Item(BaseModel):
    name: str | None = Field(
        min_length=3,
        max_length=50,
        title="Nome do item",
        description="Nome do item que será vendido",
        example="Exemplo de conteúdo",
    )
    description: str | None = None


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

@app.post("/items/post", status_code=201)
def postItem():
    return "Parabéns post enviado"

# @app.get("lista/{item_id}")
# def get_item(item_id: int, Annotated[str, Query(ge=3, le=50)] name: str):
#     return {"item_id": item_id, "name": name}