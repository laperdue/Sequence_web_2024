# flask --app .\Activité_1\app.py run --debug

from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def accueil():
    if request.method == "GET":
        miams = loadMiams()
        return render_template("index.html", miams = miams)
    
@app.route('/<season>', methods = ["GET"])
def season(season):
    if request.method == "GET":
        miams = loadMiams(season)
        return render_template("index.html", miams = miams)
    

def loadMiams(season = None):
    file = open("miam.json", "r", encoding="utf-8")
    miams = json.loads(file.read())['miams']
    file.close()
    # Filter by season
    if season:
        filteredMiams = []
        seasons = ["Hiver", "Printemps", "Été", "Automne"]
        for miam in miams:
            print(miam)
            indexStart = seasons.index(miam['debut']) 
            indexEnd = seasons.index(miam['fin'])
            indexSeason = seasons.index(season)
            if indexStart < indexEnd:
                if indexStart <= indexSeason and indexSeason <= indexEnd:
                    filteredMiams.append(miam)
            else:
                if indexStart <= indexSeason or indexSeason <= indexEnd:
                    filteredMiams.append(miam)
        miams = filteredMiams
    return miams