import json
import requests
from requests.exceptions import ConnectionError


class MovieApp:
    def __init__(self, storage):
        self._storage = storage

    def _command_list_movies(self):
        movies = self._storage.list_movies()
        print(f"\nTHERE ARE {len(movies)} MOVIES FOR YOU TO CHOOSE")
        for name, attribute in movies.items():
            print(f"{name} ({attribute[1]}): {attribute[0]}")

    def _command_add_movies(self) -> None:
        title = input("Enter new movie name: ")
        movies = self._storage.list_movies()
        if title in movies:
            print(f"Movie {title} already exist!")
            return
        api_url = 'http://www.omdbapi.com/?apikey=b49eb448&t={}'.format(title)
        try:
            response = requests.get(api_url)
            if response.status_code == requests.codes.ok:
                title = response.json()["Title"]
                year = response.json()["Year"]
                rate = float(response.json()["imdbRating"])
                poster = response.json()["Poster"]
                self._storage.add_movie(title, year, rate, poster)

                # movies.update({new_movie: [movie_rate, movie_year, movie_poster]})
                # with open("data.json", "w") as file_obj:
                #     json.dump(movies, file_obj, indent=4)
                # print(f"Movie {new_movie} successfully added")
            else:
                print("Error:", response.status_code, response.text)
        except ConnectionError as e:
            print("No internet connection!")
        except KeyError:
            print(f"Movie {title} doesn't exit!")

    def _command_movie_stats(self):
        pass

    def _generate_website(self):
        pass

    def run(self):
        while True:
            print("""
        ********** My Movies Database **********

        Menu:
        1. List movies
        0. Exit program
        """)
            choice = int(input("Enter choice (0-1): "))
            if choice == 1:
                self._command_list_movies()
            elif choice == 0:
                print("Thanks for using! Bye!")
                exit()
