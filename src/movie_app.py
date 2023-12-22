
import requests
from requests.exceptions import ConnectionError


class MovieApp:
    def __init__(self, storage):
        self._storage = storage

    def _command_list_movies(self) -> None:
        movies = self._storage.list_movies()
        print(f"\nTHERE ARE {len(movies)} MOVIES FOR YOU TO CHOOSE")
        for name, attribute in movies.items():
            print(f"{name} ({attribute[1]}): {attribute[0]}")

    def _command_add_movies(self) -> None:
        movies = self._storage.list_movies()
        title = input("Enter new movie name: ")
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
            else:
                print("Error:", response.status_code, response.text)
        except ConnectionError as e:
            print("No internet connection!")
        except KeyError:
            print(f"Movie {title} doesn't exit!")

    def _command_delete_movie(self) -> None:
        title = input("Enter movie name that you want to delete from your collection: ")
        self._storage.delete_movie(title)

    def _command_update_movie(self) -> None:
        movies = self._storage.list_movies()
        title = input("Enter movie name to update: ")
        if title in movies:
            rating = float(input("Enter new movie rating (0-10): "))
            self._storage.update_movie(title, rating)

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
        2. Add movies
        3. Delete movie
        4. Update movie rate
        0. Exit program
        """)
            choice = int(input("Enter choice (0-4): "))
            if choice == 1:
                self._command_list_movies()
            if choice == 2:
                self._command_add_movies()
            if choice == 3:
                self._command_delete_movie()
            if choice == 4:
                self._command_update_movie()
            elif choice == 0:
                print("Thanks for using! Bye!")
                exit()
