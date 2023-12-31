import csv
from istorage import IStorage


class StorageCsv(IStorage):
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def list_movies(self):
        """
                Returns a dictionary of dictionaries that
                contains the movies information in the database.

                The function loads the information from the CSV
                file and returns the data.

                For example, the function may return:
                {
                  "Titanic": [
                    9,
                    1999
                  ],
                  "..." [
                    ...
                  ],
                ]
                """

        with open(self.file_path, "r") as file:
            csv_reader = csv.DictReader(file)
            data_list = []
            for row in csv_reader:
                data_list.append(row)
            movie_data_format = {}
            for data in data_list:
                movie_data_format.update({data['title']: [data['rating'], data['year']]})

        return movie_data_format

    def add_movie(self, title, year, rating, poster):
        pass

    def delete_movie(self, title):
        pass

    def update_movie(self, title, rating):
        pass
