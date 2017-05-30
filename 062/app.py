#!python3

from flask import Flask, render_template, request
import sqlite3

with sqlite3.connect("friends.db") as connection:
    c = connection.cursor()
    try:
        c.execute("""CREATE TABLE friend_details
                (name TEXT, address TEXT, phone_number TEXT)
                """)		
    except:
        pass

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    info = []
    if request.method == 'POST' and 'name' in request.form:
        name = request.form.get('name')
        address = request.form.get('address')
        number = request.form.get('number')
        for i in (name, address, number):
            info.append(i)
        
        with sqlite3.connect("friends.db") as connection:
            c = connection.cursor()
            c.execute("INSERT INTO friend_details VALUES(?, ?, ?)", info)
    return render_template('index.html',
                            info=info)


@app.route('/friends', methods=['GET', 'POST'])
def friends():
    choice = ''
    with sqlite3.connect("friends.db") as connection:
        c = connection.cursor()
    if request.method == 'POST' and 'friend_menu' in request.form:
        choice = request.form.get('friend_menu')
    return render_template('friends.html',
                            c=c,
                            choice=choice)

app.run()