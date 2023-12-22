import json
from istorage import IStorage


class StorageCsv(IStorage):
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def list_movies(self):
        pass

    def add_movie(self, title, year, rating, poster):
        pass

    def delete_movie(self, title):
        pass

    def update_movie(self, title, rating):
        pass
