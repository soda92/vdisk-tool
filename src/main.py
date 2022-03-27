from enum import Enum
from http.client import HTTPException
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


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/model/{model_name}")
def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_name": file_path}


def attach_disk(size: str) -> str | str:
    try:
        proc = subprocess.Popen(
            "diskpart", stdin=subprocess.PIPE, stdout=subprocess.PIPE
        )
    except OSError as e:
        return None, str(e)
    else:
        proc.stdin.write(f"select vdisk file=D:\\vdisk\\vdisk_{size}.vhdx\r\n".encode())
        proc.stdin.write(b"attach vdisk\r\n")
        proc.stdin.write(b"exit\r\n")
        proc.stdin.flush()
        s = proc.communicate()
        val = s[0].decode()
        if proc.poll() is None:
            proc.terminate()
        return val, None


def detach_disk(size: str) -> str | str:
    try:
        proc = subprocess.Popen(
            "diskpart", stdin=subprocess.PIPE, stdout=subprocess.PIPE
        )
    except OSError as e:
        return None, str(e)
    else:
        proc.stdin.write(f"select vdisk file=D:\\vdisk\\vdisk_{size}.vhdx\r\n".encode())
        proc.stdin.write(b"detach vdisk\r\n")
        proc.stdin.write(b"exit\r\n")
        proc.stdin.flush()
        s = proc.communicate()
        val = s[0].decode()
        if proc.poll() is None:
            proc.terminate()
        return val, None


@app.put("/udisk")
def attach_udisk_api():
    val, err = attach_disk("100MB")
    if err:
        raise HTTPException(status_code=500, detail=err)
    return val


@app.delete("/udisk")
def attach_udisk_api():
    val, err = detach_disk("100MB")
    if err:
        raise HTTPException(status_code=500, detail=err)
    return val


@app.put("/disk")
def attach_udisk_api():
    val, err = attach_disk("1GB")
    if err:
        raise HTTPException(status_code=500, detail=err)
    return val


@app.delete("/disk")
def attach_udisk_api():
    val, err = detach_disk("1GB")
    if err:
        raise HTTPException(status_code=500, detail=err)
    return val
