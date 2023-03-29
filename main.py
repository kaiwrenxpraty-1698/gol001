"""
Context:
This code will display standard examples of Game of Life, based on the option selected
"""
import sys

from gameoflife import application


def main():
    """
    executable
    """
    try:
        option = sys.argv[1]
    except IndexError:
        option = "null"
    game_of_life_application = application.Application(option)
    game_of_life_application.start_application()


if __name__ == "__main__":
    main()
