
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    # return "hello world";
    return jsonify({"id": 1, "name": "Lucky"}), 200




