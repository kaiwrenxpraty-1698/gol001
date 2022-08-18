from time import sleep

from gameoflife.menu import select_menu_option
from gameoflife.next_generation import next_generation_of
from gameoflife.input_output import introduction, print_matrix, mask_input_matrix, summary, summary_dict


def start_application(option):
    if option == "1" or option == "2":
        introduction(option)
        first_generation_matrix = select_menu_option(option)
        next_generation_matrix = next_generation_of(first_generation_matrix)
        print_next_generation_matrix(next_generation_matrix, option)
    elif option == "3" or option == "4":
        first_generation_matrix = select_menu_option(option)
        number_of_generation = 0
        next_generation_matrix, number_of_generation = generate_first_generation_matrix(number_of_generation, first_generation_matrix)

        while number_of_generation < 10:
            next_generation_matrix = next_generation_of(next_generation_matrix)
            sleep(.5)
            print(f"Here is your output matrix -->")
            print_matrix(mask_input_matrix(next_generation_matrix))
            print(f"State of the matrix --> {number_of_generation%2}")
            number_of_generation += 1
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

def print_next_generation_matrix(next_generation_matrix, option):
    sleep(.5)
    print(f"Here is your output matrix -->")
    print_matrix(mask_input_matrix(next_generation_matrix))
    summary(option)

def generate_first_generation_matrix(number_of_generation, first_generation_matrix):
    next_generation_matrix = next_generation_of(first_generation_matrix)
    number_of_generation += 1
    return next_generation_matrix, number_of_generation
