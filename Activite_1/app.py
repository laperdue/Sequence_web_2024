# flask --app .\Activité_1\app.py run --debug

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def accueil():
    if request.method == "GET":
        return render_template("accueil.html")