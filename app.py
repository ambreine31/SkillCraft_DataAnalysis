from flask import Flask, render_template, redirect,request,url_for
from flask_restful import reqparse, abort, Api, Resource
import pickle
import pandas as pd
import numpy as np
app = Flask(__name__)
api = Api(app)

#arguments qui sont passés dans l'url de l'api
put_args = reqparse.RequestParser()
put_args.add_argument("apm", type=str, help="apm missing", required = True)
put_args.add_argument("selectbyhotkeys", type=str, help="selectbyhotkeys missing", required = True)
put_args.add_argument("assigntohotkeys", type=str, help="assigntohotkeys missing", required = True)
put_args.add_argument("uniquehotkeys", type=str, help="uniquehotkeys missing", required = True)
put_args.add_argument("minimapattacks", type=str, help="minimapattacks missing", required = True)
put_args.add_argument("minimaprightclicks", type=str, help="minimaprightclicks missing", required = True)
put_args.add_argument("numberofpacs", type=str, help="numberofpacs missing", required = True)
put_args.add_argument("gapbetweenpacs", type=str, help="gapbetweenpacs missing", required = True)
put_args.add_argument("actionlatency", type=str, help="actionlatency missing", required = True)
put_args.add_argument("actionsinpac", type=str, help="actionsinpac missing", required = True)
put_args.add_argument("totalmapexplored", type=str, help="totalmapexplored missing", required = True)
put_args.add_argument("workersmade", type=str, help="workersmade missing", required = True)
put_args.add_argument("uniqueunitsmade", type=str, help="uniqueunitsmade missing", required = True)
put_args.add_argument("complexunitsmade", type=str, help="complexunitsmade missing", required = True)
put_args.add_argument("complexabilitiesused", type=str, help="complexabilitiesused missing", required = True)

#notre API consiste en une requete GET qui récupère les données entrées par l'utilisateur et renvoie la league resultant de la prediction de notre modèle
class API(Resource):
    def get(self):
        args = put_args.parse_args()
        X = [float(args.apm), float(args.selectbyhotkeys), float(args.assigntohotkeys), float(args.uniquehotkeys), float(args.minimapattacks),
            float(args.minimaprightclicks), float(args.numberofpacs), float(args.gapbetweenpacs), float(args.actionlatency), float(args.actionsinpac),
            float(args.totalmapexplored), float(args.workersmade), float(args.uniqueunitsmade), float(args.complexunitsmade), float(args.complexabilitiesused)]
        LinReg = pickle.load( open( "LinReg.p", "rb" ) ) #on importe notre modèle de regression linéaire entrainé dans notre jupyter notebook
        LinReg_pred = LinReg.predict([X]) #prediction du modele
        pred = int(LinReg_pred[0]) #on arrondi a un int pour avoir la categorie
        if pred < 0: #on traite les valeurs extremes
            pred = 1
        if pred > 6:
            pred = 6
        Leagues = ['Bronze', 'Silver', 'Gold', 'Platinum', 'Diamond', 'Master', 'Professional']
        return redirect( url_for('result', league = Leagues[pred])) #on renvoie le nom de la categorie correspondante

api.add_resource(API, "/api/") #le lien de l'api

@app.route('/')
def main(): #page principale
    return render_template("page.html")

@app.route('/result') #page resultat de la league prédit
def result():
    league = request.args.get('league') #récupérer la league de l'api
    return render_template("result.html", league = league)


if __name__ == '__main__':
    app.run(debug=True)