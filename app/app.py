from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route("/login")
def login():
    return render_template("login.html")

app.run(debug=True)
