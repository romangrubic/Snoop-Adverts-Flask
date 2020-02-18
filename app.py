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
    return render_template('buy.html', tittle="Buy", adverts=mongo.db.advert.find({"buy":"on"}))


# --------- Selling page ----------------------------------------
@app.route('/sell')
def sell():
    return render_template('sell.html', tittle="Sell", adverts=mongo.db.advert.find({"sell":"on"}))


# --------- Single advert page ----------------------------------
@app.route('/view_advert/<advert_id>')
def view_advert(advert_id):
    advert = mongo.db.advert.find_one({'_id': ObjectId(advert_id)})
    return render_template('view_advert.html', tittle="Advert info", advert=advert)


# ----------- Add advert ----------------------------------------
@app.route('/add_advert')
def add_advert():
    return render_template('add_advert.html', tittle="Add advert", categories=mongo.db.categories.find())


# ---------- Insert advert --------------------------------------
@app.route('/insert_advert', methods=['POST'])
def insert_advert():
    advert = mongo.db.advert
    if "advert_image" in request.files:
        advert_image = request.files['advert_image']
        mongo.save_file(advert_image.filename, advert_image)

    new_advert = {
        'buy/sell': request.form.get('buy/sell'),
        'category_name': request.form.get('category_name'),
        'advert_name': request.form.get('advert_name'),
        'advert_description': request.form.get('advert_description'),
        'price': request.form.get('price'),
        'contact_info': request.form.get('contact_info'),
        'location': request.form.get('location'),
        'imageURL': advert_image.filename
        }
    advert.insert_one(new_advert)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)