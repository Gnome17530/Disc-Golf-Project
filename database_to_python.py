''' A simple program to put a database into python by Naomi 12.10.2020'''

'Imports'
import sqlite3

'Function'

DATABASE_FILE = "discgolf.db"

with sqlite3.connect(DATABASE_FILE) as connection:
    cursor = connection.cursor()
    sql = "SELECT * FROM category"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)