#!python3
#sqlite_db_check.py is a script to create a db and capture exceptions.
#The script will create a specified db on the first run.
#The exception is handy because on subsequent runs, it prints a message
#that the DB exists. It'll also print any other actual errors. Useful!

import sqlite3
import sys

with sqlite3.connect("my_database.db") as connection:
    c = connection.cursor()
    try:
        c.execute("CREATE TABLE table-name (column1 TEXT, column2 TEXT")
    except Exception as e:
        print("Could not create the database. DB either already exists or there was an error (see output below):")
        print("Exception: {}".format(str(e)))
