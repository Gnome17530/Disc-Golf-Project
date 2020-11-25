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

@app.route('/disc/<int:disc_id>')
def show_disc(disc_id):
    # show the disc with the given id, the id is an integer
    return render_template("discinfo.html", disc_id = disc_id)



if __name__ == "__main__":
    app.run(debug = True)