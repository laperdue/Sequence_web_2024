# flask --app .\Activité_1\app.py run --debug

from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def accueil():
    if request.method == "GET":
        miams = loadMiams()
        return render_template("index.html", miams = miams)
    

def loadMiams():
    file = open("miam.json", "r", encoding="utf-8")
    load = json.loads(file.read())
    return load['miams']