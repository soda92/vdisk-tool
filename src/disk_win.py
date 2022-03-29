import subprocess
import os
import shutil
import math


def convert_size(size: str):
    size = size.lower()
    if size.endswith("gb"):
        return int(size[:-2]) * 1024
    else:
        return int(size[:-2])


def delete_all():
    for file in os.listdir("D:\\vdisk"):
        if file.endswith("vhdx"):
            os.remove("D:\\vdisk\\" + file)

def get_disks():
    disks = []
    for i in "ABCDEFG":
        if os.path.exists(i + ":"):
            disks.append(i + ":/")


def select_disk(size: str):
    s0 = convert_size(size)
    for i in os.listdir("D:\\vdisk"):
        s = i.split(".")[0].split("_")[1]
        s1 = convert_size(s)
        if math.abs(s0 - s1) <= 2:
            return s


def detach_all():
    for i in get_disks():
        total, _, _ = shutil.disk_usage(i)
        total = str(int(total / 1024 / 1024)) + "MB"
        size = select_disk(total)
        detach_disk(size)


def create_disk(size: str) -> str | str:
    try:
        proc = subprocess.Popen(
            "diskpart", stdin=subprocess.PIPE, stdout=subprocess.PIPE
        )
    except OSError as e:
        return None, str(e)
    else:
        proc.stdin.write(
            f"create vdisk file=D:\\vdisk\\vdisk_{size}.vhdx type=expandable size={convert_size(size)}\r\n".encode()
        )
        proc.stdin.write(f"select vdisk file=D:\\vdisk\\vdisk_{size}.vhdx\r\n".encode())
        proc.stdin.write(f"convert mbr\r\n".encode())
        proc.stdin.write(f"create partition primary\r\n".encode())
        proc.stdin.write(f"format fs=ntfs label=vdisk{size} quick\r\n".encode())
        proc.stdin.write(b"exit\r\n")
        proc.stdin.flush()
        s = proc.communicate()
        val = s[0].decode('gbk')
        if proc.poll() is None:
            proc.terminate()
        return val, None


def attach_disk(size: str) -> str | str:
    if not os.path.exists(f"D:\\vdisk\\vdisk_{size}.vhdx"):
        create_disk(size)
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
        val = s[0].decode('gbk')
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
        val = s[0].decode('gbk')
        if proc.poll() is None:
            proc.terminate()
        return val, None
