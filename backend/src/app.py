import flask
from flask import request, json, jsonify
import requests

app = flask.Flask(__name__)
app.config["DEBUG"] = True
print("Rodou")
@app.route("/hello", methods=["GET"])
def index():
    print("ola")
    return "Ola"

if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True, port=5000)