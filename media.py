class Movie(object):

    """Movie class for use with Fresh Tomatoes.

    This class acts as a container for the parameters required by the
    Fresh Tomatoes script to display a movie in the HTML movie list.

    """

    def __init__(self, movie_title, movie_year, movie_storyline,
                 movie_poster_url, movie_trailer_url):
        """Constructor method, sets the instance variables.

        All the instance variables are mandatory for initialization, the required
        values are the movie: Title, Release Year, Storyline, Poster URL and
        YouTube Trailer URL.

        """
        self.title = movie_title
        self.year = movie_year
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_url
        self.trailer_youtube_url = movie_trailer_url
