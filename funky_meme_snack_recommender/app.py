
from flask import Flask, render_template, request
import random

app = Flask(__name__)

COMBOS = {
    "sad": {
        "meme": "sad_frog.png",
        "snack": "Double-chocolate brownie",
        "caption": "Because life feels like Ctrl+Z isn't working."
    },
    "dead inside": {
        "meme": "skull_emoji.png",
        "snack": "Cold black coffee",
        "caption": "You vibe with existential dread and stale memes."
    },
    "exam stress": {
        "meme": "exam_burnout.png",
        "snack": "Pack of Maggi & 2 Red Bulls",
        "caption": "When books scream louder than you do."
    },
    "happy": {
        "meme": "happy_rainbow.gif",
        "snack": "Waffles with rainbow syrup",
        "caption": "You're basically a walking unicorn today!"
    }
}

@app.route("/", methods=["GET", "POST"])
def index():
    mood = None
    combo = None
    if request.method == "POST":
        mood = request.form.get("mood")
        combo = COMBOS.get(mood)
    return render_template("index.html", mood=mood, combo=combo)

if __name__ == "__main__":
    app.run(debug=True)
