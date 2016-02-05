# Create a class called Movie
class Movie:
    """This module provides a way to store movie-related information."""

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, lead_actors, release_date, box_office):
        """This class returns a movie object.

        Attributes:
            movie_title (str): The movie title
            movie_storyline (str): A very brief storyline of the movie
            poster_image (str): A url to the movie poster image
            trailer_youtube (str): A url to the movie trailer on YouTube
            lead_actors (str): A short list of the movie's lead actors
            release_date (str): The release date of the movie
            box_office (str): The movie's box office figure expressed in USD
        """

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.actors = lead_actors
        self.release_date = release_date
        self.box_office = box_office
