import subprocess
from dataclasses import dataclass
from typing import List
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

from conf import *


def get_out():
    try:
        proc = subprocess.Popen(
            "diskpart", stdin=subprocess.PIPE, stdout=subprocess.PIPE
        )
    except OSError as e:
        return str(e)
    else:
        s = proc.communicate()
        proc.terminate()
        return s[0].decode()


@dataclass
class disk:
    name: str
    size: str


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


import os


def get_disks() -> List[disk]:
    if not os.path.exists(path=path):
        return []
    arr = []
    for i in os.listdir(path):
        if i.endswith(".vhdx"):
            name, size = i.split(".")[0].split("_")
            arr.append(disk(name, size))
    return arr


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_price": item.price, "item_id": item_id}
