from time import sleep

from gameoflife.next_generation import next_generation_of
from gameoflife.input_output import start_introduction, print_matrix, mask_input_matrix_values, end_summary, \
    summary_dict, output_print_statement, output_generation_statement, select_menu_option


def start_application(option):
    if option == "1" or option == "2":
        first_generation_matrix = _generate_and_print_initial_generation(option)
        _generate_and_print_next_generation(first_generation_matrix, None)
        end_summary(option)
    elif option == "3" or option == "4":
        first_generation_matrix = _generate_and_print_initial_generation(option)
        NUMBER_OF_GENERATION = 1
        next_generation_matrix, NUMBER_OF_GENERATION = _generate_and_print_second_generation(first_generation_matrix,
                                                                                             NUMBER_OF_GENERATION)
        while NUMBER_OF_GENERATION <= 10:
            next_generation_matrix, NUMBER_OF_GENERATION = _generate_and_print_next_generation(next_generation_matrix,
                                                                                               NUMBER_OF_GENERATION)
        end_summary(option)
    elif option == "5":
        first_generation_matrix = _generate_and_print_initial_generation(option)
        NUMBER_OF_GENERATION = 1
        next_generation_matrix, NUMBER_OF_GENERATION = _generate_and_print_second_generation(first_generation_matrix,
                                                                                             NUMBER_OF_GENERATION)
        while NUMBER_OF_GENERATION <= 25:
            next_generation_matrix, NUMBER_OF_GENERATION = _generate_and_print_next_generation(next_generation_matrix,
                                                                                               NUMBER_OF_GENERATION)
        end_summary(option)
    elif option == "help":
        print(summary_dict['help'])
        return 0
    else:
        print(summary_dict['error'])
        return 0


def _generate_and_print_second_generation(first_generation_matrix, number_of_generation):
    next_generation_matrix, number_of_generation = generate_second_generation_matrix(number_of_generation,
                                                                                     first_generation_matrix)
    print_next_generation_matrix(number_of_generation, next_generation_matrix)
    number_of_generation += 1
    return next_generation_matrix, number_of_generation


def _generate_and_print_next_generation(first_generation_matrix, number_of_generation=None):
    if number_of_generation is None:
        next_generation_matrix = next_generation_of(first_generation_matrix)
        print_next_generation_matrix(number_of_generation, next_generation_matrix)
    else:
        next_generation_matrix = next_generation_of(first_generation_matrix)
        print_intermediate_generation_matrix(next_generation_matrix, number_of_generation)
        number_of_generation += 1
        return next_generation_matrix, number_of_generation


def _generate_and_print_initial_generation(option):
    start_introduction(option)
    first_generation_matrix = select_menu_option(option)
    print_first_generation(first_generation_matrix)
    return first_generation_matrix


def print_first_generation(first_generation_matrix):
    output_print_statement("initial generation")
    print_matrix(mask_input_matrix_values(first_generation_matrix))
    sleep(1)


def print_next_generation_matrix(number_of_generation, next_generation_matrix):
    if number_of_generation:
        sleep(.5)
        output_print_statement("output")
        print_matrix(mask_input_matrix_values(next_generation_matrix))
        output_generation_statement(number_of_generation)
    else:
        sleep(.5)
        output_print_statement("output")
        print_matrix(mask_input_matrix_values(next_generation_matrix))


def generate_second_generation_matrix(number_of_generation, first_generation_matrix):
    next_generation_matrix = next_generation_of(first_generation_matrix)
    number_of_generation += 1
    return next_generation_matrix, number_of_generation


def print_intermediate_generation_matrix(next_generation_matrix, number_of_generation=None):
    if number_of_generation:
        sleep(.5)
        output_print_statement("output")
        print_matrix(mask_input_matrix_values(next_generation_matrix))
        output_generation_statement(number_of_generation)
