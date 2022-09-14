from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug import exceptions

app = Flask(__name__)

CORS(app)

cartoons = [
    {"id": 1, "name": "Teen Titans"},
    {"id": 2, "name": "Arthur"},
    {"id": 3, "name": "Rugrats"},
    {"id": 4, "name": "UBOS"},
    {"id": 5, "name": "Lampies"}
]


@app.route("/")
def home():
    return [c for c in cartoons], 200


# @app.route("/cartoons")
# def home1():
#     cartoon_data = request.get_json()
#     return jsonify({"all shows": cartoon_data})


# @app.route("/api/cartoons")
# def home2():
#     return jsonify({"all shows": cartoons})


# @app.route("/api/cartoons", method=["post"])
# def post_cartoon():
#     return "adds more cats when post request made"


@app.route("/api/cartoons", methods=["post", "GET"])
def add_cartoon():
    if request.method == "GET":
        return jsonify({"cartoons": cartoons})
    if request.method == "POST":
        added_cartoon = request.get_json()
        print("HERE===> ", request.get_json())
        cartoons.append(added_cartoon)
        # cartoons["id"] = int(len(cartoons))
        # print("HERE===> ", int(len(cartoons)))
        # print("HERE===> ", type(len(cartoons)))
        return jsonify({"all cartoons": cartoons})


@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return jsonify({"message": f"It's not you it's us"}, 500)


if __name__ == "__main__":
    app.run(debug=True)
