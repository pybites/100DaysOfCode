#!python3
#random_movie.py is a script to demonstrate pulling a row from an sqlite db at random.

from contextlib import contextmanager
import sqlite3

DB = "movies.db"

@contextmanager
def open_db(name):
    try:
        conn = sqlite3.connect('%s' % name)
        cursor = conn.cursor()
        yield cursor
    finally:
        conn.close()

        
def select_movie():
    with open_db(DB) as cursor:
        movie = cursor.execute("SELECT * FROM test_table ORDER BY RANDOM() LIMIT 1;")
        for i in movie:
            print("A random movie to watch is %s."  % i[0])
    return

if __name__ == "__main__":
    select_movie()