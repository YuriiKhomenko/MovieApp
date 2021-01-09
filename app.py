movies = []
START = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "


def add_film():
    title = input("Enter title of the film: ")
    year = input("Enter year of the film: ")
    director = input("Enter director of the film: ")
    genre = input("Enter genre of the film: ")
    rating = input("Enter your rating of the film: ")
    movies.append({
        'title': title,
        'year': year,
        'director': director,
        'genre': genre,
        'rating': rating
    })


def list_available_films():
    quantity = len(movies)
    titles = [movie['title'] for movie in movies]
    titles = ', '.join(titles)

    if quantity:
        print(f'You have following movies in collection: {titles}. In total you have {quantity} {"movie" if quantity == 1 else "movies"}.')
    else:
        print('There are no movies in you collection.')


def find_specific_title(title):
    for movie in movies:
        if movie['title'] == title:
            return f'''Here is information about requested title:
                    Title: {movie['title']},
                    Director: {movie['director']},
                    Year: {movie['year']},
                    Genre: {movie['genre']},
                    Rating: {movie['rating']}.'''
        else:
            return 'Requested title was not found in the collection.'


def main_process():
    selection = input(START).lower()
    while selection != 'q':
        if selection == 'a':
            add_film()
        elif selection == 'l':
            list_available_films()
        elif selection == 'f':
            title = input('Enter title of the movie: ')
            print(find_specific_title(title))
        else:
            print("Unknown command. Please choose within available options: 'a', 'f', 'l' or 'q' to close the app.")
        selection = input(START)
    print('Thank you for using the app. See you next time!')


if __name__ == '__main__':
    main_process()
