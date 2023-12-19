import operator
import random
import statistics

import movie_storage


# -----CRUD function section-----

def exit_program():
    """
        Prompt message and exit program
        """
    print("Thanks for using! Bye!")
    exit()


def stats(movies):
    """
        Calculate the average, median, min, max of the movie rates. Prompt the result
        with the message.
        """
    rate_list = []
    for movie in movies:
        rate_list.append(movies[movie][0])
    print(f"Average rating: {statistics.mean(rate_list)}")
    print(f"Median rating: {statistics.median(rate_list)}")
    for movie, stat in movies.items():
        if stat[0] == max(rate_list):
            print(f"Best movie: {movie}, {stat[0]}")
        if stat[0] == min(rate_list):
            print(f"Worst movie: {movie}, {stat[0]}")


def random_movie(movies):
    """
    Display a random movie from the json file to the user
    """
    movie, stat = random.choice(list(movies.items()))
    print(f"Your movie for tonight: {movie}, it's rated {stat[0]}")


def search_movie(movies):
    """
        Search movie base on user input. It will find the text that in the json file
        and display it.
        Example:
            - User: The
            - Result:
    The Shawshank Redemption (1994): 9.5
    The Godfather (1972): 9.2
    The Godfather: Part II (1974): 9.0
    The Dark Knight (2008): 9.0
    The Room (2003): 3.6
"""

    user_search = input("Enter part of movie name: ")
    for movie, stat in movies.items():
        if user_search.lower() in movie.lower():
            print(f"{movie} ({stat[1]}): {stat[0]}")


def sorted_by_rating(movies):
    """Sort all the movie from highest to lowest base on the rate value"""
    sort = dict(sorted(movies.items(), key=operator.itemgetter(1), reverse=True)[:len(movies)])
    for movie, stat in sort.items():
        print(f"{movie} ({stat[1]}): {stat[0]}")


def website_generator(movies):
    """
        This function will use the json file data to insert into html file with tag to create content
        for the website. Including movie title, year of production, rating and URL link to the poster of the movie
        """
    output = ""
    for movie, stat in movies.items():
        output += "<li>"
        output += "<div class='movie'>\n"
        output += f"<img class='movie-poster' src='{stat[2]}'\n>"
        output += f"<div class='movie-title'>{movie}</div>\n"
        output += f"<div class='movie-year'>{stat[1]}</dive>\n"
        output += "</div>\n"
        output += "</li>"
    with open("Test/API.py", "r") as html_file:
        html = html_file.read()
    with open("index_template.html", "w") as html_file:
        html_file.write(html.replace("__TEMPLATE_MOVIE_GRID__", output))
        print("Website was generated successfully.")


# -----MAIN-----
def main():
    # Dictionary to store the movies and the rating
    movies = movie_storage.load_data("Movie-Time/data.json")
    # Menu section
    while True:
        print("""
********** My Movies Database **********

Menu:
1. List movies
2. Add movie
3. Delete movie
4. Update movie
5. Stats
6. Random movie
7. Search movie
8. Movies sorted by rating
9. Generate website
0. Exit program
    """)

        choice = int(input("Enter choice (1-8): "))
        if choice == 1:
            print(f"\nTHERE ARE {len(movies)} MOVIES FOR YOU TO CHOOSE")
            movie_storage.list_movies(movies)
        elif choice == 2:
            movie_storage.add_movie(movies)
        elif choice == 3:
            movie_storage.delete_movie(movies)
        elif choice == 4:
            movie_storage.update_movie(movies)
        elif choice == 5:
            stats(movies)
        elif choice == 6:
            random_movie(movies)
        elif choice == 7:
            search_movie(movies)
        elif choice == 8:
            sorted_by_rating(movies)
        elif choice == 9:
            website_generator(movies)
        elif choice == 0:
            exit_program()
        else:
            print("Invalid choice")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
