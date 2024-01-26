import logging

from typing import List
from fastapi import FastAPI
from pydantic import BaseModel, Field
from uuid import uuid4, UUID

class Item(BaseModel):
    # Create a new uuid if none exist
    item_id:UUID = Field(default_factory=uuid4)
    item_name: str

# we have no items at startup
items_list: List[Item]
items_list = []

logger = logging.getLogger()
app = FastAPI()

# get an item
@app.get("/item/{item_id}")
def get_item(item_id:UUID) -> Item:
    filtered_item_list = [item for item in items_list if item.item_id == item_id]
    if filtered_item_list:
        return filtered_item_list[0]

# get all items
@app.get("/items/")
def get_items() -> List[Item]:
    print(items_list)
    return items_list

# put an item
@app.put("/item/")
def put_item(item:Item) -> Item:
    items_list.append(item)
    return item
