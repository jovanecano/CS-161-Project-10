#Author: Jovane Cano
#GitHub Account: jovanecano
#Date: 06/04/2024
# Description:
""" The program below defines a system that manages movies across different streaming services and includes classes to
represent movies, straming services, and a streaming guide"""

class Movie:
    """this class represents a movie with a title, genre, director, and year it was made"""

    def __init__(self, title, genre, director, year): # initializes a movie object
        self._title = title
        self._genre = genre
        self._director = director
        self._year = year

    def get__title(self): #method that returns the tile of the movie
        return self._title

    def get__genre(self):  # method that returns the genre of the movie
        return self._genre

    def get__director(self):  # method that returns the directr of the movie
        return self._director

    def get__year(self):  # method that returns the year of the movie
        return self._year


class StreamingService:
    """ this class represents the streaming service with name and category of movies"""

    def __init__(self, name): #initializes the SS object with given name and empty catalog
        self._name = name
        self._catalog = {}

    def get__name(self): # method to return the name of the streaming service
        return self._name

    def get__catalog(self): # method to return the name of the catalog
        return self._catalog

    def add_movie(self, movie): # method will add movie object to the catalog
        self._catalog[movie.get_title()] = movie

    def delete_movie(self, title): # this method will delete a given movie from the catalog if it already exists
        if title in self._catalog:
            del self._catalog[title]


class StreamingGuide:
    """ This class represents a guide to manage multiple streaming services and to be able to query which grants access to
    a given movie"""
    def __init__(self): # creates an empty list to add list streaming services
        self._services = []

    def add_streaming_service(self, service): #this method will add the streaming service to list
        self._services.append(service)

    def delete_streaming_service(self, name): # this method will delete the streaming service if it exists
        self._services = [service for service in self._services if service.get_name() != name]

    def who_streams_this_movie(self,title): # this method will determine which service shows a particular movie
        services_with_movies = [] #empty list that stores the name of the services that offer given movie
        movie_year = None

        for service in self._services:
            catalog = service.get_catalog()
            if title in catalog:
                services_with_movies.append(service.get_name())
                movie_year = catalog[title].get_year()

            if services_with_movies:
                return {
                'title': title,
                'year': movie_year,
                'services': services_with_movies
                }
        else:
            return None


""" Example usage from the assigment repo
if __name__ == "__main__":
    movie_1 = Movie('The Seventh Seal', 'comedy', 'Ingmar Bergman', 1957)
    movie_2 = Movie('Home Alone', 'tragedy', 'Chris Columbus', 1990)
    movie_3 = Movie('Little Women', 'action thriller', 'Greta Gerwig', 2019)
    movie_4 = Movie('Galaxy Quest', 'historical documents', 'Dean Parisot', 1999)

    stream_serv_1 = StreamingService('Netflick')
    stream_serv_1.add_movie(movie_2)

    stream_serv_2 = StreamingService('Hula')
    stream_serv_2.add_movie(movie_1)
    stream_serv_2.add_movie(movie_4)
    stream_serv_2.delete_movie('The Seventh Seal')
    stream_serv_2.add_movie(movie_2)

    stream_serv_3 = StreamingService('Dizzy+')
    stream_serv_3.add_movie(movie_4)
    stream_serv_3.add_movie(movie_3)
    stream_serv_3.add_movie(movie_1)

    stream_guide = StreamingGuide()
    stream_guide.add_streaming_service(stream_serv_1)
    stream_guide.add_streaming_service(stream_serv_2)
    stream_guide.add_streaming_service(stream_serv_3)
    stream_guide.delete_streaming_service('Hula')

    search_results = stream_guide.who_streams_this_movie('Little Women')
    print(search_results)
    
"""
