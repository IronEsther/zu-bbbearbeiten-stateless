import helper
from flask import Flask, request, Response, render_template, redirect, url_for

app = Flask(__name__)


# urls regieren
@app.route("/")
def index():
    todos = helper.get_all()
    return render_template("index.html", todos=todos)


@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    date = request.form.get("date")
    helper.add(title, date)
    return redirect(url_for("index"))


@app.route("/update/<int:index>")
def update(index):
    helper.update(index)
    return redirect(url_for("index"))
