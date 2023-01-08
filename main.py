from mapping import YEAR_FILTER_DATE, MOVIES_TYPE_MANAGED
from model import Movie, get_movies_from_db
    

def get_filtered_movies(movies: list[Movie], selected_type: str) -> list[Movie]:
    """
    Rules for filtering movies:
        The movie must be shown in the cinema;
        The movie have to be a recent movie and match the select_type or must be 5 stars noted
    """
    filtered_movies = []
    for movie in movies:
        if not movie.schedules:
            continue
        if movie.stars == 5:
            filtered_movies.append(movie)
        elif movie.type == selected_type and movie.release_year_date >= YEAR_FILTER_DATE:
            filtered_movies.append(movie)
    return filtered_movies

def get_best_movie(filtered_movies: list[Movie]) -> Movie:
    sorted_movies = sorted(filtered_movies, key=lambda movie: movie.release_year_date, reverse=True)
    return next(iter(sorted_movies), None)

def get_selected_movie_type() -> str:
    while True:
        selected_type = input(f"Choose the type of the movie you want to watch (managed movie type : {MOVIES_TYPE_MANAGED}): ")
        if selected_type in MOVIES_TYPE_MANAGED:
            return selected_type
        else:
            print(f"Bad film genre, please choose one in the managed movie type")


def choose_movie_to_watch(movies: list[Movie]) -> Movie:
    selected_type = get_selected_movie_type()

    filtered_movies = get_filtered_movies(movies, selected_type)
    if not filtered_movies:
        print("Error, not movie left with the given criteria")
        return None

    decided_movie = get_best_movie(filtered_movies)
    if not decided_movie:
        print("Internal error | 500")
    decided_movie.display_infos()

    return decided_movie

def main():
    movies = get_movies_from_db()
    movie_to_watch = choose_movie_to_watch(movies)

    # The function can continue

if __name__ == "__main__":
    main()

    