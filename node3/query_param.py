# query_param.py
from fastapi import FastAPI

# Create a FastAPI instance
app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

@app.get("/items/{item_id}")
def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item