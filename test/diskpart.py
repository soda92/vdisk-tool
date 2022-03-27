import subprocess

try:
    proc = subprocess.Popen("diskpart", stdin=subprocess.PIPE, stdout=subprocess.PIPE)
except OSError as e:
    print(e)
    exit(0)
else:
    proc.stdin.write(b"select vdisk file=D:\\vdisk\\vdisk_100MB.vhdx\r\n")
    proc.stdin.write(b"attach vdisk\r\n")
    proc.stdin.flush()
    s = proc.communicate()
    print(s[0].decode())
    proc.terminate()
