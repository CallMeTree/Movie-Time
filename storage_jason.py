import json

from istorage import IStorage


class StorageJson(IStorage):
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def list_movies(self):
        with open(self.file_path, "r") as handle:
            movies = json.load(handle)
        for name, attribute in movies.items():
            print(f"{name} ({attribute[1]}): {attribute[0]}")

    def add_movie(self, title, year, rating, poster):
        ...

    def delete_movie(self, title):
        ...

    def update_movie(self, title, rating):
        ...