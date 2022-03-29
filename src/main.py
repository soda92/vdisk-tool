from http.client import HTTPException
from disk_win import *
from fastapi import FastAPI
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger(__name__)

# TODO: add clear api
def clear():
    pass


app = FastAPI()


@app.delete("/all")
def delete_all_vdisk_files():
    delete_all()


@app.put("/udisk")
def attach_udisk_api():
    val, err = attach_disk("100MB")
    if err:
        raise HTTPException(status_code=500, detail=err)
    logger.info(val)
    return val


@app.delete("/udisk")
def detach_udisk_api():
    val, err = detach_disk("100MB")
    if err:
        raise HTTPException(status_code=500, detail=err)
    logger.info(val)
    return val


@app.put("/disk")
def attach_disk_api():
    val, err = attach_disk("1GB")
    if err:
        raise HTTPException(status_code=500, detail=err)
    logger.info(val)
    return val


@app.delete("/disk")
def detach_disk_api():
    val, err = detach_disk("1GB")
    if err:
        raise HTTPException(status_code=500, detail=err)
    logger.info(val)
    return val
