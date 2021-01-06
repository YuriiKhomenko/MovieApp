movies = []
START = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "


def main_process():
    selection = input(START)
    while selection != 'q':
        if selection == 'a':
            pass
        elif selection == 'l':
            pass
        elif selection == 'f':
            pass
        else:
            print("Unknown command. Please choose within available options: 'a', 'f', 'l' or 'q' to close the app.")
        selection = input(START)
    print('Thank you for using the app. See you next time!')


if __name__ == '__main__':
    main_process()
