# code from 030
from contextlib import contextmanager
import sqlite3

DB = 'pycon.sqlite'


@contextmanager
def conn_db():
    try:
        conn = sqlite3.connect(DB)
        conn.row_factory = sqlite3.Row  # want dict rows, thanks Row
        cursor = conn.cursor()
        yield cursor
    finally:
        conn.commit()
        conn.close()
