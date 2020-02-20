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


# --------- Marketplace page ----------------------------------------
@app.route('/marketplace')
def marketplace():
    return render_template('marketplace.html', tittle="Marketplace", adverts=mongo.db.advert.find())


# --------- Filter: Motors ------------------------------------
@app.route('/motors_and_vehicles')
def motors_and_vehicles():
    return render_template('marketplace.html', tittle="Motors and vehicles", adverts=mongo.db.advert.find({'category_name': 'Motors and vehicles'}))


# --------- Filter: Home ------------------------------------
@app.route('/home_garden_diy')
def home_garden_diy():
    return render_template('marketplace.html', tittle="Home, garden and DIY", adverts=mongo.db.advert.find({'category_name': 'Home, garden, DIY'}))


# --------- Filter: Home ------------------------------------
@app.route('/pc_stuff_and_games')
def pc_stuff_and_games():
    return render_template('marketplace.html', tittle="PC stuff and games", adverts=mongo.db.advert.find({'category_name': 'PC stuff and games'}))


# ----------- Filter: Search ------------------------------------
@app.route('/search', methods=['GET', 'POST'])
def search():
    query = request.args.get('search').upper()
    results = mongo.db.advert.find({'advert_name': {"$regex": query}})
    results_number = results.count()
    return render_template("search.html", tittle="Search", results=results, results_number=results_number)



# --------- Single advert page ----------------------------------
@app.route('/view_advert/<advert_id>')
def view_advert(advert_id):
    advert = mongo.db.advert.find_one({'_id': ObjectId(advert_id)})
    return render_template('view_advert.html', tittle="Advert info", advert=advert)


# ----------- Add advert ----------------------------------------
@app.route('/add_advert')
def add_advert():
    return render_template('add_advert.html', tittle="Add advert", categories=mongo.db.categories.find(), counties=mongo.db.county.find())


# ---------- Insert advert --------------------------------------
@app.route('/insert_advert', methods=['POST'])
def insert_advert():
    advert = mongo.db.advert

    if "advert_image" in request.files:
        advert_image = request.files['advert_image']
        mongo.save_file(advert_image.filename, advert_image)

    new_advert = {
        'category_name': request.form.get('category_name'),
        'advert_name': request.form.get('advert_name').upper(),
        'advert_description': request.form.get('advert_description'),
        'price': request.form.get('price'),
        'contact_info': request.form.get('contact_info'),
        'location': request.form.get('location'),
        'imageURL': advert_image.filename
    }
    advert.insert_one(new_advert)
    return redirect(url_for('marketplace'))


# ------------ Uploading ---------------------------------------
@app.route('/file/<filename>')
def file(filename):
    return mongo.send_file(filename)


# ------------- Edit advert ------------------------------------
@app.route('/edit_advert/<advert_id>', methods=['GET'])
def edit_advert(advert_id):
    the_advert = mongo.db.advert.find_one({"_id": ObjectId(advert_id)})
    all_categories = mongo.db.categories.find()
    return render_template('edit_advert.html', tittle="Edit Advert",  advert=the_advert, categories=all_categories, counties=mongo.db.county.find())


# ------------ Update advert -----------------------------------
@app.route('/update_advert/<advert_id>', methods=['POST'])
def update_advert(advert_id):
    advert = mongo.db.advert.find_one({"_id": ObjectId(advert_id)})

    if 'advert_image' in request.files and request.files['advert_image'].filename != "":
        advert_image = request.files['advert_image']
        image_filename = advert_image.filename
        mongo.save_file(advert_image.filename, advert_image)
    else:
        image_filename = advert['imageURL']

    mongo.db.advert.update({'_id': ObjectId(advert_id)},
    {
        'category_name': request.form.get('category_name'),
        'advert_name': request.form.get('advert_name').upper(),
        'advert_description': request.form.get('advert_description'),
        'price': request.form.get('price'),
        'contact_info': request.form.get('contact_info'),
        'location': request.form.get('location'),
        'imageURL': image_filename
    })
    return redirect(url_for('view_advert', advert_id=advert_id))


# ------------------ Deleting advert ---------------------------
@app.route('/delete_advert/<advert_id>')
def delete_advert(advert_id):
    advert = mongo.db.advert
    advert.remove({'_id': ObjectId(advert_id)})
    return redirect(url_for('marketplace'))


# ------------- Host/Port/Debug --------------------------------
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)