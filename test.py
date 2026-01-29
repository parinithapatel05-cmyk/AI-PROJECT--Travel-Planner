print("Python file started")

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask is working!"

print("Before app.run")

app.run(host="127.0.0.1", port=5000)

print("After app.run")
