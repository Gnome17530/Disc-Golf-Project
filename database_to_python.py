''' A simple program to put a database into python by Naomi 12.10.2020

'Imports'
import sqlite3

'Function'

DATABASE_FILE = "discgolf.db"

with sqlite3.connect(DATABASE_FILE) as connection:
    cursor = connection.cursor()
    sql = "SELECT * FROM category"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)'''

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
    return render_template("contents.html", results=results)


if __name__ == "__main__":
    app.run(debug = True)