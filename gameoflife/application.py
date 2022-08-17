from time import sleep

from gameoflife.select_input_matrix import select_from_matrix_option
from gameoflife.core import implement_game_of_life
from gameoflife.helper import introduction, print_matrix, mask_input_matrix, summary, summary_dict


def start_application(option):
    if option == "1" or option == "2":
        introduction(option)
        matrix = select_from_matrix_option(option)
        matrix = implement_game_of_life(matrix)
        print(f"Here is your output matrix -->")
        print_matrix(mask_input_matrix(matrix))
        summary(option)
    elif option == "3" or option == "4":
        from gameoflife import select_input_matrix
        matrix = select_input_matrix.select_from_matrix_option(option)
        count = 0
        while count < 10:
            matrix = implement_game_of_life(matrix)
            sleep(.5)
            print(f"Here is your output matrix -->")
            print_matrix(mask_input_matrix(matrix))
            print(f"State of the matrix --> {count%2}")
            count += 1
        summary(option)
    elif option == "5":
        matrix = select_from_matrix_option(option)
        count = 0
        while count < 25:
            matrix = implement_game_of_life(matrix)
            sleep(.75)
            print(f"Here is your output matrix -->")
            print_matrix(mask_input_matrix(matrix))
            count += 1
        summary(option)
    elif option == "help":
        print(summary_dict['help'])
        return 0
    else:
        print(summary_dict['error'])
        return 0
