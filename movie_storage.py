import json

import requests
from requests.exceptions import ConnectionError


def load_data(file_path):
    with open(file_path, "r") as handle:
        return json.load(handle)


def list_movies(movies):
    """
        Returns a dictionary of dictionaries that
        contains the movies information in the database.

        The function loads the information from the JSON
        file and returns the data.

        For example, the function may return:
        {
          "Titanic": {
            "rating": 9,
            "year": 1999
          },
          "..." {
            ...
          },
        }
        """

    for name, attribute in movies.items():
        print(f"{name} ({attribute[1]}): {attribute[0]}")


def add_movie(movies):
    """
        Adds a movie to the movie database.
        Loads the information from the API database, add the movie to the JSON file,
        and saves it. The function doesn't need to validate the input.
        """

    title = input("Enter new movie name: ")
    api_url = 'http://www.omdbapi.com/?apikey=b49eb448&t={}'.format(title)
    try:
        response = requests.get(api_url)
        if response.status_code == requests.codes.ok:
            new_movie = response.json()["Title"]
            movie_year = response.json()["Year"]
            movie_rate = float(response.json()["imdbRating"])
            movie_poster = response.json()["Poster"]
            movies.update({new_movie: [movie_rate, movie_year, movie_poster]})
            with open("data.json", "w") as file_obj:
                json.dump(movies, file_obj, indent=4)
            print(f"Movie {new_movie} successfully added")
        else:
            print("Error:", response.status_code, response.text)
    except ConnectionError as e:
        print("No internet connection!")
    except KeyError:
        print(f"Movie {title} doesn't exit!")


def delete_movie(movies):
    """
        Deletes a movie from the movie database.
        Loads the information from the JSON file, deletes the movie,
        and saves it. The function doesn't need to validate the input.
        """

    movie = input("Enter movie name to delete: ")
    if movie in movies:
        del movies[movie]

        with open("data.json", "w") as file_obj:
            json.dump(movies, file_obj, indent=4)
            print(f"""Movie "{movie}" successfully deleted""")
    else:
        print(f"""Movie "{movie}" doesn't exit""")


def update_movie(movies):
    """
        Updates a movie from the movie database.
        Loads the information from the JSON file, updates the movie,
        and saves it. The function doesn't need to validate the input.
        """

    movie = input("Enter movie name to update: ")
    if movie in movies:
        rate = float(input("Enter new movie rating (0-10): "))
        movies[movie][0] = rate
        with open("data.json", "w") as file_obj:
            json.dump(movies, file_obj, indent=4)
            print(f"""Movie "{movie}" successfully updated""")
    else:
        print(f"""Movie "{movie}" doesn't exit""")
