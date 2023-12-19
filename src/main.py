from movie_app import MovieApp
from storage_jason import StorageJson


def main():
    storage = StorageJson("../data/data.json")
    movie_app = MovieApp(storage)
    movie_app.run()


if __name__ == "__main__":
    main()
