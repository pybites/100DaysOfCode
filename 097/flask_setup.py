#!python3
#flask_setup.py is a script to create a default Flask dir setup to start work
#on new Flask projects.

import os

project = input("Please specify a new project path. Folder will be created: ")

os.mkdir(project)
os.chdir(project)
os.mkdir("templates")
os.mkdir("static")
open('app.py', 'w').close()
os.chdir(project + "/templates")
open('index.html', 'w').close()
os.chdir(project + "/static")
open('style.css', 'w').close()
