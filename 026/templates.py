TEMPLATE = '''
Title: {Title}
Year: {Year}
Genre: {Genre}
Director: {Director}
Actors: {Actors}
IMDB score: {imdbRating}
Plot: {Plot}

'''
HTML_TEMPLATE = '''
<li>
    <h1>{Title} ({Year})</h1>
    <h2>Genre: {Genre} / Director: {Director}</h2>
    <h3>Actors: {Actors}</h3>
    <h4>IMDB score: {imdbRating}</h4>
    <p>{Plot}</p>
</li>
'''
