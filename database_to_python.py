''' A simple program to put a database into python by Naomi 12.10.2020'''

from flask import Flask,g, render_template, request, redirect

import sqlite3

app = Flask(__name__)

DATABASE = 'discgolf.db'


def get_db():
    db = getattr(g, '_list', None)
    if db is None:
        db = g._list = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_list', None)
    if db is not None:
        db.close()
    
@app.route("/")
def home():
    cursor = get_db().cursor()
    sql = "SELECT * FROM disc"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template("disc.html", results=results)

@app.route('/add' , methods=["GET","POST"])
def add():
    if request.method == "POST":
        cursor = get_db().cursor()
        new_img = request.form["item_img"]
        new_description = request.form["item_description"]
        new_category = request.form["item_category"]
        sql = "INSERT INTO disc(img url, description, category) VALUES (?, ?, ?)"
        cursor.execute(sql(new_img, new_description, new_category))
        get_db().commit()
    return redirect('/')

@app.route('/delete', methods=["GET", "POST"])
def delete():
    if request.method == "POST":
        #get the item and deleting it from the database
        cursor = get_db().cursor()
        id = int(request.form["item_category"])
        sql = "DELETE FROM disc WHERE id=?"

if __name__ == "__main__":
    app.run(debug = True)