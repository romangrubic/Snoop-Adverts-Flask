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
# --------- Landing page // Home page ---------------------------
@app.route('/landing-page')
def landing_page():
    return render_template('landing-page.html')


# --------- Buying page -----------------------------------------
@app.route('/buy')
def buy():
    return render_template('buy.html')


# --------- Selling page ----------------------------------------
@app.route('/sell')
def sell():
    return render_template('sell.html')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)