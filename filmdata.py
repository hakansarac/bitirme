from imdb import IMDb
from random import randrange

class TopMovies:
    def __init__(self):
        moviesDB = IMDb()
        self.top = moviesDB.get_top250_movies() 
        self.movieID = randrange(251)

    def search_mov(self):
        return self.top[self.movieID]['title']

    def movie_year(self):
        return self.top[self.movieID]['year']


