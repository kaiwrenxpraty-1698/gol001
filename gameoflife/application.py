from time import sleep

from gameoflife.menu import select_menu_option
from gameoflife.next_generation import next_generation_of
from gameoflife.input_output import introduction, print_matrix, mask_input_matrix, end_summary, summary_dict


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
            print_intermediate_generation_matrix(number_of_generation, next_generation_matrix)
            number_of_generation += 1
        end_summary(option)
    elif option == "5":
        first_generation_matrix = select_menu_option(option)
        number_of_generation = 0
        next_generation_matrix, number_of_generation = generate_first_generation_matrix(number_of_generation, first_generation_matrix)
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



def print_next_generation_matrix(next_generation_matrix, option):
    sleep(.5)
    print(f"Here is your output matrix -->")
    print_matrix(mask_input_matrix(next_generation_matrix))
    end_summary(option)


def generate_first_generation_matrix(number_of_generation, first_generation_matrix):
    next_generation_matrix = next_generation_of(first_generation_matrix)
    number_of_generation += 1
    return next_generation_matrix, number_of_generation



def print_intermediate_generation_matrix(number_of_generation, next_generation_matrix):
    sleep(.5)
    print(f"Here is your output matrix -->")
    print_matrix(mask_input_matrix(next_generation_matrix))
    print(f"Generation of the matrix --> {number_of_generation}")