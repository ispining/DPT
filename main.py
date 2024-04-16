from AI import Dark
import flask
from flask import request, jsonify
import json

app = flask.Flask(__name__)


@app.route("/chat/v1/completions", methods=["POST"])
def generate():
    data = request.json
    if data.get("user_id"):
        user_id = data["user_id"]
    else:
        api_key = data["api_key"]
        user_id = api_key.split("-")[0]

    dpt = Dark(user_id)
    if request.json.get("history"):
        history = request.json["history"]
    else:
        history = []

    resp = dpt.generate(history)
    only_text = dpt.get_text_only(resp)
    return jsonify({"role": "assistant", "text": only_text})


if __name__ == "__main__":
    app.run(debug=True)
