from home import app
from flask import Flask, render_template


@app.route("/")
def index():
    return render_template("login.html")
