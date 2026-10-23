import random
import string

from flask import Flask, jsonify, request

app = Flask(__name__)

links = {}


def generate_code(length=6):
    chars = string.ascii_letters + string.digits
    return "".join(random.choices(chars, k=length))


@app.route("/")
def home():
    return "Hello Shortly"


@app.route("/health")
def health():
    return jsonify(status="ok")


@app.route("/shorten", methods=["POST"])
def shorten():
    data = request.get_json(silent=True) or {}
    url = data.get("url")
    if not url or not url.startswith(("http://", "https://")):
        return jsonify(error="URL invalide"), 400
    code = generate_code()
    links[code] = url
    return jsonify(code=code), 201


if __name__ == "__main__":
    app.run(port=5000)
