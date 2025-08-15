from flask import Flask, render_template, request, redirect, url_for
import socket, time
from functions import scores  # משתמשים באותה רשימה מה-CLI

app = Flask(__name__)

def calc_average():
    if not scores:
        return None
    return round(sum(s["score"] for s in scores) / len(scores), 2)

@app.route("/")
def index():
    avg = calc_average() if request.args.get("average") else None
    now_ms = int(time.time() * 1000)
    host = socket.gethostname()
    return render_template("index.html", scores=scores, average=avg, host=host, now_ms=now_ms)

@app.route("/sort/<key>")
def sort_view(key):
    key = key.lower()
    reverse = key == "score"
    if key not in {"name", "game", "score"}:
        key = "name"
        reverse = False
    sorted_list = sorted(scores, key=lambda x: x[key], reverse=reverse)
    avg = calc_average() if request.args.get("average") else None
    now_ms = int(time.time() * 1000)
    host = socket.gethostname()
    return render_template("index.html", scores=sorted_list, average=avg, host=host, now_ms=now_ms)

@app.post("/add")
def add():
    name = request.form.get("name","").strip()
    game = request.form.get("game","").strip()
    score = float(request.form.get("score","0"))
    scores.append({"name": name, "game": game, "score": score})
    return redirect(url_for("index"))

@app.post("/delete")
def delete():
    name = request.form.get("name","").strip()
    game = (request.form.get("game") or "").strip()
    if game:
        to_keep = [s for s in scores if not (s["name"] == name and s["game"] == game)]
    else:
        to_keep = [s for s in scores if s["name"] != name]
    scores[:] = to_keep
    return redirect(url_for("index"))

@app.post("/edit")
def edit():
    current_name = request.form.get("current_name","").strip()
    current_game = request.form.get("current_game","").strip()
    new_name = (request.form.get("new_name") or "").strip()
    new_game = (request.form.get("new_game") or "").strip()
    new_score = (request.form.get("new_score") or "").strip()

    for s in scores:
        if s["name"] == current_name and s["game"] == current_game:
            if new_name:
                s["name"] = new_name
            if new_game:
                s["game"] = new_game
            if new_score:
                try:
                    s["score"] = float(new_score)
                except ValueError:
                    pass
            break
    return redirect(url_for("index"))

if __name__ == "__main__":
    # חשוב: 0.0.0.0 כדי שהשירות יהיה נגיש מחוץ לקונטיינר
    app.run(host="0.0.0.0", port=5000)
