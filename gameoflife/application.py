from time import sleep

from gameoflife.next_generation import NextGeneration
from gameoflife.input_output import InputOutput

def start_application(option):
    '''
    core function to generate next generation based on the input option
    '''
    if option == "1" or option == "2":
        first_generation_matrix = _generate_and_print_initial_generation(option)
        _generate_and_print_next_generation(first_generation_matrix, None)
        InputOutput(option, None).end_summary()
    elif option == "3" or option == "4":
        first_generation_matrix = _generate_and_print_initial_generation(option)
        NUMBER_OF_GENERATION = 1
        next_generation_matrix, NUMBER_OF_GENERATION = _generate_and_print_second_generation(first_generation_matrix,
                                                                                             NUMBER_OF_GENERATION)
        while NUMBER_OF_GENERATION <= 10:
            next_generation_matrix, NUMBER_OF_GENERATION = _generate_and_print_next_generation(next_generation_matrix,
                                                                                               NUMBER_OF_GENERATION)
        InputOutput(option, None).end_summary()
    elif option == "5":
        first_generation_matrix = _generate_and_print_initial_generation(option)
        NUMBER_OF_GENERATION = 1
        next_generation_matrix, NUMBER_OF_GENERATION = _generate_and_print_second_generation(first_generation_matrix,
                                                                                             NUMBER_OF_GENERATION)
        while NUMBER_OF_GENERATION <= 25:
            next_generation_matrix, NUMBER_OF_GENERATION = _generate_and_print_next_generation(next_generation_matrix,
                                                                                               NUMBER_OF_GENERATION)
        InputOutput(option, None).end_summary()
    elif option == "help":
        print(InputOutput(None, None).summary_dict['help'])
        return 0
    else:
        print(InputOutput(None, None).summary_dict['error'])
        return 0


def _generate_and_print_second_generation(first_generation_matrix, number_of_generation):
    next_generation_matrix, number_of_generation = generate_second_generation_matrix(number_of_generation,
                                                                                     first_generation_matrix)
    print_next_generation_matrix(number_of_generation, next_generation_matrix)
    number_of_generation += 1
    return next_generation_matrix, number_of_generation


def _generate_and_print_next_generation(first_generation_matrix, number_of_generation=None):
    if number_of_generation is None:
        next_generation = NextGeneration(first_generation_matrix)
        next_generation_matrix = next_generation.next_generation_of()
        print_next_generation_matrix(number_of_generation, next_generation_matrix)
    else:
        next_generation = NextGeneration(first_generation_matrix)
        next_generation_matrix = next_generation.next_generation_of()
        print_intermediate_generation_matrix(next_generation_matrix, number_of_generation)
        number_of_generation += 1
        return next_generation_matrix, number_of_generation


def _generate_and_print_initial_generation(option):
    input_output = InputOutput(option)
    input_output.start_introduction()
    first_generation_matrix = input_output.select_menu_option()
    print_first_generation(first_generation_matrix)
    return first_generation_matrix


def print_first_generation(first_generation_matrix):
    '''
    prints first generation of the input template with static information for the user
    '''
    input_output = InputOutput(None, first_generation_matrix)
    input_output.output_print_statement("initial generation")
    input_output.mask_input_matrix_values()
    input_output.print_matrix()
    sleep(1)


def print_next_generation_matrix(number_of_generation, next_generation_matrix):
    input_output = InputOutput(None, next_generation_matrix)
    if number_of_generation:
        sleep(.5)
        input_output.output_print_statement("output")
        input_output.mask_input_matrix_values()
        input_output.print_matrix()
        input_output.output_generation_statement(number_of_generation)
    else:
        sleep(.5)
        input_output.output_print_statement("output")
        input_output.mask_input_matrix_values()
        input_output.print_matrix()


def generate_second_generation_matrix(number_of_generation, first_generation_matrix):
    next_generation = NextGeneration(first_generation_matrix)
    next_generation_matrix = next_generation.next_generation_of()
    number_of_generation += 1
    return next_generation_matrix, number_of_generation


def print_intermediate_generation_matrix(next_generation_matrix, number_of_generation=None):
    input_output = InputOutput(None, next_generation_matrix)
    if number_of_generation:
        sleep(.5)
        input_output.output_print_statement("output")
        input_output.mask_input_matrix_values()
        input_output.print_matrix()
        input_output.output_generation_statement(number_of_generation)
