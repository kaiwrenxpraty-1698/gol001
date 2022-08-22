'''
submodule to program input output
'''
from gameoflife.constants import DEAD
from gameoflife.menu import Menu

class InputOutput:
    '''
    Class responsible for static response, user interface and flow control of the application
    '''
    summary_dict = {
    "1" :"This is the most common still life pattern of Game of Life: Block. \nKey point: the state of matrix is identical to the input matrix.",
    "2":"This is the another common still life pattern of Game of Life: Bee-hive. \nKey point: the state of matrix is identical to the input matrix.",
    "3":"This is a popular oscillator pattern of Game of Life: Blinker. \nKey point: the matrix reaches its initial state after exactly 2 iterations, hence the pattern keeps oscillating.",
    "4":"This is a popular oscillator pattern of Game of Life: Toad. \nKey point: the matrix reaches its initial state after exactly 2 iterations, hence the pattern keeps oscillating.",
    "5":"This is the most popular Spaceships pattern of Game of Life: Glider. \nKey point: the pattern keeps gliding over the matrix",
    "help": "Welcome to the Game of Life.\nPlease select the option number corresponding to the pattern, you will like to print: \n1. Block \n2. Bee-Hive \n3. Blinker \n4. Toad \n5. Glider",
    "error":"Sorry this option is not valid, please add help argument to know how the tool works",
    "mapping":{
        "1": "Block",
        "2": "Bee-Hive",
        "3": "Blinker",
        "4": "Toad",
        "5": "Glider"
}
}
    def __init__(self, option=None, matrix=None):
        self.option = option
        self.matrix = matrix

    def start_introduction(self):
        '''
        method to load introduction summary from the summary dictionary
        '''
        name_of_pattern = self.summary_dict['mapping'][self.option]
        print(f'Welcome to the Game of Life; So glad that you have chosen: {name_of_pattern}')

    def end_summary(self):
        '''
        method to load ending summary from the summary dictionary
        '''
        print(self.summary_dict[self.option])

    def print_matrix(self):
        '''
        method to print matrix
        '''
        for idx in range(len(self.matrix)):
            print(self.matrix[idx])

    def output_print_statement(self, state):
        '''
        method to print dynamic strings
        '''
        print(f"Here is your {state} matrix -->")
    
    def output_generation_statement(self, number_of_generation):
        '''
        method to print generation of iteration dynamically
        '''
        print(f"Generation of the matrix --> {number_of_generation}")

    def mask_input_matrix_values(self): 
        '''
        method to mask underlying nummeric values with constants
        '''
        output_matrix = [[] for _ in range(len(self.matrix))]
        for idx in range(len(self.matrix)):
            for idx2 in range(len(self.matrix[0])):
                if self.matrix[idx][idx2] == DEAD:
                    output_matrix[idx].append(" ")
                else:
                    output_matrix[idx].append("ALIVE")
        return output_matrix
    
    def select_menu_option(self):
        '''
        method to select options from the Menu class
        '''
        menu = Menu(self.option)
        if menu.is_valid_option():
            return menu.grid_for_option()
        else:
            exit()