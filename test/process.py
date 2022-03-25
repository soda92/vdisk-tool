import subprocess

try:
    proc = subprocess.Popen("diskpart", stdin = subprocess.PIPE, stdout=subprocess.PIPE)
except OSError as e:
    print(e)
    exit(0)
else:
    s = proc.communicate()
    print(s[0].decode())
    proc.terminate()
