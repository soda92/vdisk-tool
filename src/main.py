from flask import Flask
import subprocess

app = Flask(__name__)


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


@app.route("/")
def hello_world():
    return f"<pre>{get_out()}</pre>"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5002)
