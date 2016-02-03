# Top Movies

A simple Python data structure for storing movie-related information. An accompanying module generates data into an HTML file.


## Details

The data structure is stored in the media.py module. This module contains a class called `Movie`. Each movie object has the following attributes: title, storyline, poster image, trailer url, lead actors, release date, and box office details.

The fresh_tomatoes.py module generates an HTML file which displays the instances of the `Movie` class. Included in the module is the `open_movies_page` function, which takes one argument: `movies` (a list contained in the entertainment_center.py file). Calling the `open_movies_page` function generates an HTML file displaying all of the objects of the `Movie` class.

The entertainment_center.py file includes six preloaded instances of the `Movie` class. These are put together in a list called `movies`.


## Instal instructions

Top Movies can be installed through GitHub. Navigate to https://github.com/bencam/top-movies and select the 'Download ZIP' button.


## Usage

To generate an HTML file displaying the six preloaded instances of the `Movie` class, simply run the entertainment_center.py file:

`$ python entertainment_center.py`

An HTML page will be created displaying each instance of the `Movie` class. Click on an object in order to view the movie trailer video that corresponds to the instance.

To edit the instances of the `Movie` class, open the entertainment_center.py file and delete and add (calling the `Movie` class) objects as desired. Please note that each object must be included in the `movies` list.

HTML and JavaScript elements can be altered in the fresh_tomatoes.py module.


## License

Top Movies is released under the [MIT License](http://opensource.org/licenses/MIT).
