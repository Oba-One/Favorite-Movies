"""Defines the Movie class that contains the details of a movie."""

import webbrowser

class Movie(object):
    """This class stores movie information
    Attributes:
        title: A string storing the title of the film.
        storyline: A string storing a sentence of the film plot.
        poster_image_url: A string storing the URI  of the film poster image
        trailer_youtube_id: A string storing the URI of the film trailer.
        release_date: A string storing the release date of the film.
    """
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, movie_release_date):
        """Initializes Movie class instance variables."""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_date = movie_release_date

    def show_trailer(self):
        """Plays the movie trailer in the web browser."""
        webbrowser.open(self.trailer_youtube_url)
