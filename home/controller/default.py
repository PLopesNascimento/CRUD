from home import app
from flask import Flask, render_template


@app.route("/")
def index():
    return render_template("curriculo.html")
@app.route("/login")
def login():
    return render_template("login.html")
