from flask import Flask, jsonify, render_template
import random
import json
import os

app = Flask(__name__)


def load_cards(filename):
    with open(os.path.join("data", filename), "r", encoding="utf-8") as f:
        return json.load(f)


MOTIVATION_CARDS = load_cards("motivation_cards.json")
DEMOTIVATION_CARDS = load_cards("demotivation_cards.json")


@app.route("/get-motivation")
def get_motivation():
    index = random.randint(0, len(MOTIVATION_CARDS) - 1)
    card = MOTIVATION_CARDS[index]
    return jsonify(
        {
            "text": card["text"],
            "icon": card["icon"],
            "author": card["author"],
            "index": index + 1,
            "total": len(MOTIVATION_CARDS),
        }
    )


@app.route("/get-demotivation")
def get_demotivation():
    index = random.randint(0, len(DEMOTIVATION_CARDS) - 1)
    card = DEMOTIVATION_CARDS[index]
    return jsonify(
        {
            "text": card["text"],
            "icon": card["icon"],
            "author": card["author"],
            "index": index + 1,
            "total": len(DEMOTIVATION_CARDS),
        }
    )


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=40001)
