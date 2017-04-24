## 026

Interactive script to query the [OMDb API](http://www.omdbapi.com):

	$ python omdb.py
	Script to query OMDb API
	Enter IMDB ID or title (q to exit): tt0104348

	Title: Glengarry Glen Ross
	Year: 1992
	Genre: Crime, Drama, Mystery
	Director: James Foley
	Actors: Al Pacino, Jack Lemmon, Alec Baldwin, Alan Arkin
	IMDB score: 7.8
	Plot: An examination of the machinations behind the scenes at a real estate office.


	Enter IMDB ID or title (q to exit): scarface
	Year of release? 1983

	Title: Scarface
	Year: 1983
	Genre: Crime, Drama
	Director: Brian De Palma
	Actors: Al Pacino, Steven Bauer, Michelle Pfeiffer, Mary Elizabeth Mastrantonio
	IMDB score: 8.3
	Plot: In Miami in 1980, a determined Cuban immigrant takes over a drug cartel and succumbs to greed.


	Enter IMDB ID or title (q to exit): nonsense
	Year of release? 111
	Error: Movie not found!
	Enter IMDB ID or title (q to exit): q
	Bye
	$ python omdb.py -h
	Script to query OMDb API
	Enter IMDB ID or title (q to exit): scarface
	Year of release? 1983

	<li>
		<h1>Scarface (1983)</h1>
		<h2>Genre: Crime, Drama / Director: Brian De Palma</h2>
		<h3>Actors: Al Pacino, Steven Bauer, Michelle Pfeiffer, Mary Elizabeth Mastrantonio</h3>
		<h4>IMDB score: 8.3</h4>
		<p>In Miami in 1980, a determined Cuban immigrant takes over a drug cartel and succumbs to greed.</p>
	</li>

	Enter IMDB ID or title (q to exit): q
	Bye
