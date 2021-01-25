# OMDB_and_TasteDive_Mashup
## Description:
This project will take us through the process of mashing up data from two different APIs to make movie recommendations. The TasteDive API lets us provide a movie (or bands, TV shows, etc.) as a query input, and returns a set of related items. The OMDB API lets us provide a movie title as a query input and get back data about the movie, including scores from various review sites (Rotten Tomatoes, IMDB, etc.).  We will put those two together. We will use TasteDive to get related movies for a whole list of titles. We’ll combine the resulting lists of related movies, and sort them according to their Rotten Tomatoes scores (which will require making API calls to the OMDB API.)
## Requirements:
- This code needs [Python 3](https://www.python.org/) to run.
- This code require 2 modules
  - json module (To manage .json format).
  - request module (To create a valid url format and request data from that url).
## Execution:
1. You need to provide a list of movies you want to sort recommendations for.
2. This list should be passed as a formal parameter to 'get_sorted_recommendations()' function.
3. Return value of this function will be a [rotten tomatoes](https://www.rottentomatoes.com/) rating sorted (highest rating to lowest rating) list of recommendation
