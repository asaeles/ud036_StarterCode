import webbrowser

class Movie(object):
	""" Holds the class varibles required for displaying a movie
	in Fresh Tomatoes HTML generator and playing its YouTube trailer"""

	def __init__(self, movie_title, movie_year, movie_storyline,
	movie_poster_url, movie_trailer_url):
		""" Constructor method, sets the instance variables """
		self.title = movie_title
		self.year = movie_year
		self.storyline = movie_storyline
		self.poster_image_url = movie_poster_url
		self.trailer_youtube_url = movie_trailer_url

	def play_youtube_video(self):
		""" Displays the YouTube trailer associated with
		the movie within the same web-browser page """
		webbrowser.open(self.trailer_youtube_url)
