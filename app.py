from flask import Flask, render_template_string, request, redirect, url_for
import socket
import time

app = Flask(__name__)

# מבנה נתונים פנימי (In-Memory)
scores = []

INDEX_HTML = """<<<ה-HTML שהבאת>>>
"""  # פשוט תדביק פה את ה־HTML שלך במקום <<<ה-HTML שהבאת>>>

@app.route("/")
def index():
    average = None
    if request.args.get("average"):
        if scores:
            average = sum(s["score"] for s in scores) / len(scores)
    return render_template_string(
        INDEX_HTML,
        scores=scores,
        average=average,
        host=socket.gethostname(),
        now_ms=int(time.time() * 1000)
    )

@app.route("/add", methods=["POST"])
def add_score():
    name = request.form["name"]
    game = request.form["game"]
    score = float(request.form["score"])
    scores.append({"name": name, "game": game, "score": score})
    return redirect(url_for("index"))

@app.route("/delete", methods=["POST"])
def delete_score():
    name = request.form["name"]
    game = request.form.get("game")
    global scores
    if game:
        scores = [s for s in scores if not (s["name"] == name and s["game"] == game)]
    else:
        scores = [s for s in scores if s["name"] != name]
    return redirect(url_for("index"))

@app.route("/edit", methods=["POST"])
def edit_score():
    current_name = request.form["current_name"]
    current_game = request.form["current_game"]

    for s in scores:
        if s["name"] == current_name and s["game"] == current_game:
            if request.form["new_name"]:
                s["name"] = request.form["new_name"]
            if request.form["new_game"]:
                s["game"] = request.form["new_game"]
            if request.form["new_score"]:
                s["score"] = float(request.form["new_score"])
            break
    return redirect(url_for("index"))

@app.route("/sort/<key>")
def sort_view(key):
    reverse = key == "score"
    sorted_scores = sorted(scores, key=lambda s: s[key], reverse=reverse)
    average = None
    return render_template_string(
        INDEX_HTML,
        scores=sorted_scores,
        average=average,
        host=socket.gethostname(),
        now_ms=int(time.time() * 1000)
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
