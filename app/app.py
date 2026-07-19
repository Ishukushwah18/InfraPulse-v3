from flask import Flask, render_template
import subprocess
import socket
import os
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)

# -----------------------------
# Devices / Servers to Monitor
# -----------------------------
TARGETS = [
    {
        "name": "Google DNS",
        "host": "8.8.8.8",
        "port": 53
    },
    {
        "name": "Cloudflare DNS",
        "host": "1.1.1.1",
        "port": 53
    },
    {
        "name": "GitHub",
        "host": "github.com",
        "port": 443
    }
]


# -----------------------------
# Ping Check
# -----------------------------
def ping_host(host):
    try:
        result = subprocess.run(
            ["ping", "-c", "1", host],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if result.returncode == 0:
            return "Up"
        else:
            return "Down"

    except Exception:
        return "Down"
    
# -----------------------------
# Port Check
# -----------------------------
def check_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)

        result = sock.connect_ex((host, port))

        sock.close()

        if result == 0:
            return "Open"
        else:
            return "Closed"

    except Exception:
        return "Closed"
# -----------------------------
# Dashboard Route
# -----------------------------

@app.route("/health")
def health():
    return {
        "status": "healthy",
        "application": os.getenv("APP_NAME"),
        "version": os.getenv("APP_VERSION")
    }


@app.route("/")
def dashboard():

    dashboard_data = []

    for target in TARGETS:

        dashboard_data.append({

            "name": target["name"],
            "host": target["host"],
            "ping": ping_host(target["host"]),
            "port_status": check_port(target["host"], target["port"])

        })

    return render_template(
    "index.html",
    targets=dashboard_data,
    app_name=os.getenv("APP_NAME"),
    version=os.getenv("APP_VERSION")
   )


# -----------------------------
# Run Application
# -----------------------------
if __name__ == "__main__":

    app.run(
    host=os.getenv("FLASK_HOST"),
    port=int(os.getenv("FLASK_PORT")),
    debug=os.getenv("FLASK_DEBUG") == "True"
)