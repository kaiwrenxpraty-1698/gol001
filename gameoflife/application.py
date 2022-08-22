from time import sleep

from gameoflife.next_generation import NextGeneration
from gameoflife.input_output import InputOutput

class Application:
    '''
    parent class of the application
    '''
    def __init__(self, option):
        self.option = option

    def start_application(self):
        '''
        core function to generate next generation based on the input option
        '''
        if self.option == "1" or self.option == "2":
            first_generation_matrix = self._generate_and_print_initial_generation(self.option)
            self._generate_and_print_next_generation(first_generation_matrix, None)
            InputOutput(self.option, None).end_summary()
        elif self.option == "3" or self.option == "4":
            first_generation_matrix = self._generate_and_print_initial_generation(self.option)
            NUMBER_OF_GENERATION = 1
            next_generation_matrix, NUMBER_OF_GENERATION = self._generate_and_print_second_generation(first_generation_matrix,
                                                                                                NUMBER_OF_GENERATION)
            while NUMBER_OF_GENERATION <= 10:
                next_generation_matrix, NUMBER_OF_GENERATION = self._generate_and_print_next_generation(next_generation_matrix,
                                                                                                NUMBER_OF_GENERATION)
            InputOutput(self.option, None).end_summary()
        elif self.option == "5":
            first_generation_matrix = self._generate_and_print_initial_generation(self.option)
            NUMBER_OF_GENERATION = 1
            next_generation_matrix, NUMBER_OF_GENERATION = self._generate_and_print_second_generation(first_generation_matrix,
                                                                                                NUMBER_OF_GENERATION)
            while NUMBER_OF_GENERATION <= 25:
                next_generation_matrix, NUMBER_OF_GENERATION = self._generate_and_print_next_generation(next_generation_matrix,
                                                                                                NUMBER_OF_GENERATION)
            InputOutput(self.option, None).end_summary()
        elif self.option == "help":
            print(InputOutput(None, None).summary_dict['help'])
            return 0
        else:
            print(InputOutput(None, None).summary_dict['error'])
            return 0


    def _generate_and_print_second_generation(self, first_generation_matrix, number_of_generation):
        next_generation_matrix, number_of_generation = self.generate_second_generation_matrix(number_of_generation,
                                                                                        first_generation_matrix)
        self.print_next_generation_matrix(number_of_generation, next_generation_matrix)
        number_of_generation += 1
        return next_generation_matrix, number_of_generation


    def _generate_and_print_next_generation(self, first_generation_matrix, number_of_generation=None):
        if number_of_generation is None:
            next_generation = NextGeneration(first_generation_matrix)
            next_generation_matrix = next_generation.next_generation_of()
            self.print_next_generation_matrix(number_of_generation, next_generation_matrix)
        else:
            next_generation = NextGeneration(first_generation_matrix)
            next_generation_matrix = next_generation.next_generation_of()
            self.print_intermediate_generation_matrix(next_generation_matrix, number_of_generation)
            number_of_generation += 1
            return next_generation_matrix, number_of_generation


    def _generate_and_print_initial_generation(self, option):
        input_output = InputOutput(option)
        input_output.start_introduction()
        first_generation_matrix = input_output.select_menu_option()
        self.print_first_generation(first_generation_matrix)
        return first_generation_matrix


    def print_first_generation(self, first_generation_matrix):
        '''
        prints first generation of the input template with static information for the user
        '''
        input_output = InputOutput(None, first_generation_matrix)
        input_output.print_matrix(input_output.mask_input_matrix_values())
        sleep(1)


    def print_next_generation_matrix(self, number_of_generation, next_generation_matrix):
        input_output = InputOutput(None, next_generation_matrix)
        if number_of_generation:
            sleep(.5)
            input_output.output_print_statement("output")
            input_output.print_matrix(input_output.mask_input_matrix_values())
            input_output.output_generation_statement(number_of_generation)
        else:
            sleep(.5)
            input_output.output_print_statement("output")
            input_output.print_matrix(input_output.mask_input_matrix_values())


    def generate_second_generation_matrix(self, number_of_generation, first_generation_matrix):
        next_generation = NextGeneration(first_generation_matrix)
        next_generation_matrix = next_generation.next_generation_of()
        number_of_generation += 1
        return next_generation_matrix, number_of_generation


    def print_intermediate_generation_matrix(self, next_generation_matrix, number_of_generation=None):
        input_output = InputOutput(None, next_generation_matrix)
        if number_of_generation:
            sleep(.5)
            input_output.output_print_statement("output")
            input_output.print_matrix(input_output.mask_input_matrix_values())
            input_output.output_generation_statement(number_of_generation)
