#!python3
#generator to create an sqlite3 test database file with the name of your choice

#TODO - expand functionality to allow user specification of table name, number of cols, col names and types.

from contextlib import contextmanager
import sqlite3

name = ""

@contextmanager
def create_db(name):
	try:
		conn = sqlite3.connect('%s.db' % name)
		cursor = conn.cursor()
		yield cursor
	finally:
		conn.close()


def prompt_for_name():
	name = input("What would you like to name your test db file?: ")
	return name

if __name__ == "__main__":
	name = prompt_for_name()
	with create_db(name) as cursor:
		cursor.execute("""CREATE TABLE test_table
						(col1 TEXT, col2 TEXT, col3 TEXT, col4 INT)
						""")
		print('%s.db has been created' % name)
