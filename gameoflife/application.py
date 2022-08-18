from time import sleep

from gameoflife.menu import select_menu_option
from gameoflife.next_generation import next_generation_of
from gameoflife.input_output import start_introduction, print_matrix, mask_input_matrix_values, end_summary, summary_dict


def start_application(option):
    if option == "1" or option == "2":
        first_generation_matrix = _generate_and_print_initial_generation_(option)

        next_generation_matrix = next_generation_of(first_generation_matrix)
        print_next_generation_matrix(next_generation_matrix)

        end_summary(option)
    elif option == "3" or option == "4":
        start_introduction(option)
        first_generation_matrix = select_menu_option(option)
        print_first_generation(first_generation_matrix)

        number_of_generation = 0
        next_generation_matrix, number_of_generation = generate_second_generation_matrix(number_of_generation, first_generation_matrix)
        print_next_generation_matrix(next_generation_matrix)
        number_of_generation += 1

        while number_of_generation < 10:
            next_generation_matrix = next_generation_of(next_generation_matrix)
            print_intermediate_generation_matrix(number_of_generation, next_generation_matrix)
            number_of_generation += 1
        end_summary(option)
    elif option == "5":
        start_introduction(option)
        first_generation_matrix = select_menu_option(option)
        number_of_generation = 0

        next_generation_matrix, number_of_generation = generate_second_generation_matrix(number_of_generation, first_generation_matrix)
        print_next_generation_matrix(next_generation_matrix)

        while number_of_generation < 25:
            next_generation_matrix = next_generation_of(next_generation_matrix)
            print_intermediate_generation_matrix(number_of_generation, next_generation_matrix)
            number_of_generation += 1
        end_summary(option)
    elif option == "help":
        print(summary_dict['help'])
        return 0
    else:
        print(summary_dict['error'])
        return 0


def _generate_and_print_initial_generation_(option):
    start_introduction(option)
    first_generation_matrix = select_menu_option(option)
    print_first_generation(first_generation_matrix)
    return first_generation_matrix


def print_first_generation(first_generation_matrix):
    print(f"Here is your initial generation matrix -->")
    print_matrix(mask_input_matrix_values(first_generation_matrix))
    sleep(1)


def print_next_generation_matrix(next_generation_matrix):
    sleep(.5)
    print(f"Here is your output matrix -->")
    print_matrix(mask_input_matrix_values(next_generation_matrix))
    

def generate_second_generation_matrix(number_of_generation, first_generation_matrix):
    next_generation_matrix = next_generation_of(first_generation_matrix)
    number_of_generation += 1
    return next_generation_matrix, number_of_generation


def print_intermediate_generation_matrix(number_of_generation, next_generation_matrix):
    sleep(.5)
    print(f"Here is your output matrix -->")
    print_matrix(mask_input_matrix_values(next_generation_matrix))
    print(f"Generation of the matrix --> {number_of_generation}")