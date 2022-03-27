from http.client import HTTPException
import subprocess
from fastapi import FastAPI


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

# TODO: add clear api
def clear():
    pass

app = FastAPI()


@app.put("/udisk")
def attach_udisk_api():
    val, err = attach_disk("100MB")
    if err:
        raise HTTPException(status_code=500, detail=err)
    return val


@app.delete("/udisk")
def detach_udisk_api():
    val, err = detach_disk("100MB")
    if err:
        raise HTTPException(status_code=500, detail=err)
    return val


@app.put("/disk")
def attach_disk_api():
    val, err = attach_disk("1GB")
    if err:
        raise HTTPException(status_code=500, detail=err)
    return val


@app.delete("/disk")
def detach_disk_api():
    val, err = detach_disk("1GB")
    if err:
        raise HTTPException(status_code=500, detail=err)
    return val
