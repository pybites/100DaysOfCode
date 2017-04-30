import json
from pprint import pformat 

from flask import Flask, Response, render_template, request, jsonify
from flask_jsglue import JSGlue

from movies import get_movies, get_movie_info

app = Flask(__name__)
jsglue = JSGlue(app)

movies_by_title = {r['movie_title'] for r in get_movies()}
movies_by_id = {r['id']: r for r in get_movies()}

@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    search = request.args.get('q')
    filtered_movies = [m for m in movies_by_title 
                       if search.lower() in m.lower()]
    return jsonify(matching_results=sorted(filtered_movies))

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("main.html")

@app.route('/movie/<int:movie_id>')
def show_movie(movie_id):
    movie =  movies_by_id.get(movie_id)
    return render_template("movie.html", movie=movie, pp=pformat)


if __name__ == '__main__':
    app.run(debug=True)
