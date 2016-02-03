# The comment below enables display of the accent marks in an actor's name
# -*- coding: utf-8 -*-


# Import the fresh_tomatoes.py and media.py files
import fresh_tomatoes
import media


# Create six instances of the Movie class
star_wars = media.Movie("Star Wars: A New Hope",
                        "A handful of people save the universe",
                        "https://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=nywPf1p-BBY",
                        "Mark Hamill, Harrison Ford, Carrie Fisher",
                        "25 May 1977",
                        "$775.4 million")

the_sting = media.Movie("The Sting",
                        "A couple of grifters pull of a big con",
                        "https://upload.wikimedia.org/wikipedia/en/9/9c/Stingredfordnewman.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=LN2hBOIXhBs",
                        "Paul Newman, Robert Redford, Robert Shaw",
                        "25 December 1973",
                        "$159.6 million")

nacho_libre = media.Movie("Nacho Libre",
                          "A friar becomes a professional wrestler",
                          "https://upload.wikimedia.org/wikipedia/en/3/35/Nachopost.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=Hf_Ai6K8jFA",
                          "Jack Black, Héctor Jiménez, Ana de la Reguera",
                          "16 June 2006",
                          "$99.2 million")

k_pax = media.Movie("K-Pax",
                    "A psychiatric patient claims he is an alien",
                    "https://upload.wikimedia.org/wikipedia/en/e/e4/Kpax.jpg",  # NOQA
                    "https://www.youtube.com/watch?v=UfcbshzkvUs",
                    "Kevin Spacey, Jeff Bridges",
                    "26 October 2001",
                    "$65 million")

butch_cassidy = media.Movie("Butch Cassidy and the Sundance Kid",
                            "Outlaws at their best",
                            "https://upload.wikimedia.org/wikipedia/en/f/fd/Butch_sundance_poster.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=X41Ylp02NRs",
                            "Paul Newman, Robert Redford, Katharine Ross",
                            "24 October 1969",
                            "$102.3 million in North America")

despicable_me = media.Movie("Despicable Me",
                            "A supervillain adopts three girls and tries to steal the moon",  # NOQA
                            "https://upload.wikimedia.org/wikipedia/en/d/db/Despicable_Me_Poster.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=nVwae09eSpo",
                            "Steve Carell, Jason Segel",
                            "9 July 2010",
                            "$543.1 million")


# Create a list called movies made up of each object of the Movie class
movies = [star_wars, the_sting, nacho_libre, k_pax,
          butch_cassidy, despicable_me]


# Call the open_movies_page function in the fresh_tomatoes.py module
# This will display the instances of the Movie class on an html page
fresh_tomatoes.open_movies_page(movies)
