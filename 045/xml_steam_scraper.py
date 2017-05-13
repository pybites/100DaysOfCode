#!python3
# steam_scraper.py is a simple web scraper to check for the latest steam games

from collections import namedtuple
import sqlite3

import feedparser

FEED_FILE = "newreleases.xml"
Game = namedtuple('Game', 'Link')
games_list = []

def check_create_db():
	with sqlite3.connect("steam_games.db") as connection:
		c = connection.cursor()
		try:
			c.execute("""CREATE TABLE new_steam_games
					(N
					ame TEXT, Link TEXT)
					""")		
		except:  
			pass

def db_connection():
	with sqlite3.connect("steam_games.db") as connection:
		c = connection.cursor()
	return c
			
def main():
	
	check_create_db()
	feed = feedparser.parse(FEED_FILE)
	for entry in feed['entries']:
		Game = (entry['title'], entry['link'])
		games_list.append(Game)
	
		c = db_connection()
		c.executemany("INSERT INTO new_steam_games VALUES(?, ?)", games_list)
	

if __name__ == "__main__":
	main()
