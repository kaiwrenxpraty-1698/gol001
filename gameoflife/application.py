from time import sleep

from gameoflife.menu import select_menu_option
from gameoflife.next_generation import next_generation_of
from gameoflife.input_output import introduction, print_matrix, mask_input_matrix, summary, summary_dict


def start_application(option):
    if option == "1" or option == "2":
        introduction(option)
        matrix = select_menu_option(option)
        matrix = next_generation_of(matrix)
        print(f"Here is your output matrix -->")
        print_matrix(mask_input_matrix(matrix))
        summary(option)
    elif option == "3" or option == "4":
        matrix = select_menu_option(option)
        count = 0
        while count < 10:
            matrix = next_generation_of(matrix)
            sleep(.5)
            print(f"Here is your output matrix -->")
            print_matrix(mask_input_matrix(matrix))
            print(f"State of the matrix --> {count%2}")
            count += 1
        summary(option)
    elif option == "5":
        matrix = select_menu_option(option)
        count = 0
        while count < 25:
            matrix = next_generation_of(matrix)
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
