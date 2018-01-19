import webbrowser


class Movie(object):
	'''
	Behaviour: Creates the movie class.
	Input: The title of the movie, the storyline, image and trailer.
	Outputs: The created movie.
	'''
	def __init__(self, movie_title, movie_storyline, poster_image,
					trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
	
	def show_trailer(self):
		'''
		Behaviour: This fuction plays the trailer of the movie.
		Input: The Movie Class.
		Outputs: Plays the trailer of the movie.
		'''
		return webbrowser.open(self.trailer_youtube_url)
