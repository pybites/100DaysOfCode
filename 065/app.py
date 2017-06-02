#!python3

from flask import Flask, render_template, request, session, redirect, url_for, escape
import webbrowser

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():	
    return render_template("index.html")

webbrowser.open('http://127.0.0.1:5000')
app.run()