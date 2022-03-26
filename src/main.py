import subprocess
from dataclasses import dataclass
from typing import List
from typing import Optional
from fastapi import FastAPI

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
