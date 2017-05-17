#A useful code snippet for adding sqlite db data to an email
#The code will then update a "flag" column called "Emailed" to indicate that
#the data in that row has been emailed.
#
#To begin with, all rows should have a '0' in the Emailed column to allow
#this to work.
#
#The secondary assumption here is that you'll have your emailer set up already.
#See Day 11 emailer.py: https://github.com/pybites/100DaysOfCode/tree/master/011
#

body = ''

with sqlite3.connect("my.db") as connection:
    c = connection.cursor()
    c.execute("SELECT {data-to-be-mailed} FROM {table_name} WHERE Emailed='0'")
    for item in c.fetchall():
		#in this example I'm taking the first two columns from the db
        body += item[0] + ': ' + item[1] + '\n'
    c.execute("UPDATE table_name SET Emailed='1'")
