#pip install xlrd
from flask import Flask,render_template,request
import pandas as pd
import geopandas  as gpd
import contextily
import matplotlib.pyplot as plt


app = Flask(__name__)   #variabile che identifica il sito web

ricarica_colonnine=pd.read_csv("ricarica_colonnine.csv",sep=";")

@app.route('/', methods=['GET'])  #sono tutte le possibili richieste del utente
def home():
    trova = input("inserisci colonnine in qwuartiere: ")
    geo = dfG3857[dfG3857["nome_nil"] == trova].plot(figsize = (12, 12))
    ax = geo
    ctx.add_basemap(ax= ax)


    moviesGenres = df[~df['Genres'].str.contains('\|')]['Genres'].to_list()
    moviesGenres = list(set(geo))
    return render_template('form2.html', moviesGenres = moviesGenres )

@app.route('/risultato0', methods=['GET'])  #sono tutte le possibili richieste del utente
def homefis():
    moviesGenres = df[~df['Genres'].str.contains('\|')]['Genres'].to_list()
    moviesGenres = list(set(moviesGenres))
    return render_template('form2.html', moviesGenres = moviesGenres )

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)    #fà partire il programma