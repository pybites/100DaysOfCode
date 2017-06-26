#!python3
#This app runs an overtime tracker web app.

from flask import Flask, render_template, request
import sqlite3
import sys

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    data = []
    if request.method == 'POST' and 'date' in request.form:
        date = request.form.get('date')
        start = request.form.get('start')
        end = request.form.get('end')
        hours = request.form.get('hours')
        rate = request.form.get('rate')
        for i in (date, start, end, hours, rate):
            data.append(i)
        write_to_db(data)
    ot_list = pull_data()
    return render_template('index.html',
                            data=data,
                            ot_list=ot_list)
    
def write_to_db(data):
    with sqlite3.connect("overtime.db") as connection:
        c = connection.cursor()
        c.execute("INSERT INTO overtime_list VALUES(?, ?, ?, ?, ?)", data)
    print('Data written to DB')

    
def pull_data():
    with sqlite3.connect("overtime.db") as connection:
        c = connection.cursor()
        ot_list = c.execute("SELECT * from overtime_list")
    return ot_list
    

def check_for_db():
    with sqlite3.connect("overtime.db") as connection:
        c = connection.cursor()
        try:
            c.execute("CREATE TABLE overtime_list (Date TEXT, Start TEXT, End TEXT, Total_Hrs NUM, Rate NUM)")		
        except Exception as e:
            print("Exception: {}".format(str(e)))
            

if __name__ == "__main__":
    check_for_db()
    app.run()
