#!python3
#This is the application script for launching a Python Timezone List Flask Web App.

from flask import Flask, render_template, request
import pendulum
import pytz

app = Flask(__name__)

#Create the list to populate the pull-down menu
def create_list():
    tz_list = []
    for tz in pytz.all_timezones:
        tz_list.append(tz)
    return tz_list


@app.route('/', methods=['GET', 'POST'])
def index():
    tz_list = create_list()
    choice = ''
    tz_time = ''
    if request.method == 'POST' and 'tz_menu' in request.form:
        choice = request.form.get('tz_menu')
        tz_time = pendulum.now(choice).to_datetime_string()
    return render_template('index.html',
                            tz_list=tz_list,
                            choice=choice,
                            tz_time=tz_time)

    
if __name__ == "__main__":
    app.run()
    