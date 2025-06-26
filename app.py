from flask import Flask, jsonify
from math_utils import add, subtract

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"message": "CI/CD Demo working!"})

@app.route("/add/<int:a>/<int:b>")
def add_route(a, b):
    return jsonify({"result": add(a, b)})

@app.route("/subtract/<int:a>/<int:b>")
def add_route(a, b):
    return jsonify({"result": subtract(a, b)})

if __name__ == "__main__":
    app.run(debug=True)
