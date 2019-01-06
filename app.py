import os
from flask import Flask, redirect, url_for, render_template
from pymongo import MongoClient
from analysis import avg, probGenres

app = Flask(__name__)

client = MongoClient(
  os.environ['IMDB_MONGODB_1_PORT_27017_TCP_ADDR'],
  27017)
db = client.filmsdb
   
@app.route('/')
def imdb():
  _items = db.films.find()
  items = [item for item in _items]
  return render_template('imdb.html', items = items, avg = avg, probGenres = probGenres)

if __name__ == "__main__":
  app.run(host = '0.0.0.0', debug = True)