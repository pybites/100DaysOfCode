#!python3
#This Flask app displays photos in a directory. The app will eventually allow you to display photos
#based on file name search criteria. ie: Searching for "2017" will display all photos with 2017 in their
#file name.

from flask import Flask, render_template
import glob

PATH = "static/images/"

app = Flask(__name__)

@app.route('/')
def index():
    photo_list = get_photos()
    return render_template('index.html',
                            photo_list=photo_list)


def get_photos():
    photo_list = []
    for name in sorted(glob.glob(PATH + "*")):
        photo_list.append(name)
    return photo_list

if __name__ == "__main__":
    app.run()
