from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def init():
    return redirect(url_for("login"))

@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        redirect(url_for("home"))
    else:
        return render_template("login.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/user=<usr>")
def profile(usr):
    return render_template("profile.html")



app.run(debug=True)
