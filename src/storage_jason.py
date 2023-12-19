import json
from istorage import IStorage


class StorageJson(IStorage):
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def list_movies(self):
        with open(self.file_path, "r") as handle:
            movies = json.load(handle)
        return movies

    def add_movie(self, title, year, rating, poster):
        movies = self.list_movies()
        if title in movies:
            print(f"Movie {title} already exist!")
            return

    def delete_movie(self, title):
        pass

    def update_movie(self, title, rating):
        pass
