'''
Context:
This code will display standard examples of Game of Life, based on the option selected
'''
import sys

from gameoflife import application


def main():
    try:
        option = sys.argv[1]
    except IndexError:
        option = "null"

    application.start_application(option)


if __name__ == "__main__":
    main()
