from src import APIrequest

x = APIrequest.MovieFinder(['28'])
print(x.movies_found)
x.searchMovieData("Shang-Chi and the Legend of the Ten Rings")
print(x.movies_data)
