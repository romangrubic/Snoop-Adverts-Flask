import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
  import env 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'adverts'
app.config["MONGO_URI"] = os.environ.get('MONGO_DATA_URI')

mongo = PyMongo(app)


@app.route('/')
# --------- Home page -------------------------------------------
@app.route('/home')
def home():
    return render_template('home.html', tittle="Home")


# --------- Buying page -----------------------------------------
@app.route('/buy')
def buy():
    return render_template('buy.html', tittle="Buy")


# --------- Selling page ----------------------------------------
@app.route('/sell')
def sell():
    return render_template('sell.html', tittle="Sell")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)