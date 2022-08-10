'''
Context:
This code will display standard examples of Game of Life, based on the option selected
'''
from time import sleep
import sys

arg_desc = '''\
    'Welcome to the Game of Life. 
    Please select the option number corresponding to the pattern, you will like to print: 
    1. Block 
    2. Bee-Hive 
    3. Blinker 
    4. Toad 
    5. Glider
'''

summary_dict ={
    '1' :'''This is the most common still life pattern of Game of Life: Block
key point: the state of matrix is identical to the input matrix.''',
    '2':'''This is the another common still life pattern of Game of Life: Bee-hive 
key point: the state of matrix is identical to the input matrix.''',
    '3':'''This is a popular oscillator pattern of Game of Life: Blinker 
key point: the matrix reaches its initial state after exactly 2 iterations, hence the pattern keeps oscillating.''',
    '4':'''This is a popular oscillator pattern of Game of Life: Toad 
key point: the matrix reaches its initial state after exactly 2 iterations, hence the pattern keeps oscillating.''',
    '5':'''This is the most popular Spaceships pattern of Game of Life: Glider 
key point: the pattern keeps gliding over the matrix''',
    'help': arg_desc,
    'error':'Sorry this option is not valid, please add help argument to know how the tool works',
    'mapping':{
        '1': 'Block',
        '2': 'Bee-Hive',
        '3': 'Blinker',
        '4': 'Toad',
        '5': 'Glider'
    }
}

def initiate_program():
    option = sys.argv[1]
    if option != "help":
        print_matrix(mask_input_matrix(select_matrix_option(option)))
        return option
    else:
        print(summary_dict[option])
        return option

def select_matrix_option(option):
    live_cell, dead_cell = 1, 0
    if option == "1":
        matrix = [[dead_cell, dead_cell, dead_cell, dead_cell], [dead_cell, live_cell, live_cell, dead_cell], [dead_cell, live_cell, live_cell, dead_cell], [dead_cell, dead_cell, dead_cell, dead_cell]]
    elif option == "2":
        matrix = [[dead_cell, dead_cell, dead_cell, dead_cell, dead_cell, dead_cell], [dead_cell, dead_cell, live_cell, live_cell, dead_cell, dead_cell], [dead_cell, live_cell, dead_cell, dead_cell, live_cell, dead_cell], [dead_cell, dead_cell, live_cell, live_cell, dead_cell, dead_cell], [dead_cell, dead_cell, dead_cell, dead_cell, dead_cell, dead_cell]]
    elif option == "3":
        matrix = [[dead_cell, dead_cell, dead_cell, dead_cell, dead_cell], [dead_cell, dead_cell, live_cell, dead_cell, dead_cell], [dead_cell, dead_cell, live_cell, dead_cell, dead_cell], [dead_cell, dead_cell, live_cell, dead_cell, dead_cell], [dead_cell, dead_cell, dead_cell, dead_cell, dead_cell]]
    elif option == "4":
        matrix = [[dead_cell, dead_cell, dead_cell, dead_cell, dead_cell, dead_cell], [dead_cell, dead_cell, dead_cell, live_cell, dead_cell, dead_cell], [dead_cell, live_cell, dead_cell, dead_cell, live_cell, dead_cell], [dead_cell, live_cell, dead_cell, dead_cell, live_cell, dead_cell], [dead_cell, dead_cell, live_cell, dead_cell, dead_cell, dead_cell], [dead_cell, dead_cell, dead_cell, dead_cell, dead_cell, dead_cell]]
    elif option == "5":
        matrix = [[dead_cell, live_cell, dead_cell, dead_cell, dead_cell, dead_cell, dead_cell, dead_cell, dead_cell, dead_cell], [dead_cell, dead_cell, live_cell, dead_cell, dead_cell, dead_cell, dead_cell, dead_cell, dead_cell, dead_cell], [live_cell, live_cell, live_cell, dead_cell, dead_cell, dead_cell, dead_cell, dead_cell, dead_cell, dead_cell]] + [[dead_cell for _ in range(10)] for _ in range(7)]
    elif option == "help":
            print(arg_desc)
    else:
        print(summary_dict['error'])
        exit()
    return matrix

def print_matrix(matrix):
    for idx in range(len(matrix)):
            print(matrix[idx])

def mask_input_matrix(matrix): 
    output_matrix = [[] for _ in range(len(matrix))]
    for idx in range(len(matrix)):
        for idx2 in range(len(matrix[0])):
            if matrix[idx][idx2] == 0:
                output_matrix[idx].append(" ")
            else:
                output_matrix[idx].append("ALIVE")
    return output_matrix
                
def implement_game_of_life(matrix):
    output_matrix = [[] for _ in range(len(matrix))]
    m, n = len(matrix), len(matrix[0])
    for i in range(m):
        for j in range(n):
            living_cells = 0
            for x in range(max(i - 1, 0), min(i + 2, m)):
                for y in range(max(j - 1, 0), min(j + 2, n)):
                    if x == i and y == j:
                        continue
                    living_cells += matrix[x][y] % 2        
            output_matrix[i].append(living_cells)

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                if output_matrix[i][j] == 2 or output_matrix[i][j] == 3:
                    output_matrix[i][j] = 1   
                else:
                    output_matrix[i][j] = 0
            else:
                if output_matrix[i][j] == 3:
                    output_matrix[i][j] = 1
                else:
                    output_matrix[i][j] = 0
                    
    return output_matrix

def start_application(option):
    def summary(option):
        print(summary_dict[option])
    
    def introduction(option):
        name_of_pattern = summary_dict['mapping'][option]
        print(f'Welcome to the Game of Life; So glad that you have chosen {name_of_pattern}')

    if option == "1" or option == "2":
        introduction(option)
        matrix = select_matrix_option(option)
        output_matrix = implement_game_of_life(matrix)
        masked_matrix = mask_input_matrix(output_matrix)
        print(f"Here is your output matrix -->")
        print_matrix(masked_matrix)
        summary(option)    
    elif option == "3" or option == "4":
        matrix = select_matrix_option(option)
        count = 0
        while count < 10:
            matrix = implement_game_of_life(matrix)
            masked_matrix = mask_input_matrix(matrix)
            sleep(.5)
            print(f"Here is your output matrix -->")
            print_matrix(masked_matrix)
            print(f"State of the matrix --> {count%2}")
            count += 1
        summary(option)
    elif option == "5":
        matrix = select_matrix_option(option)
        count = 0
        while count < 25:
            matrix = implement_game_of_life(matrix)
            masked_matrix = mask_input_matrix(matrix)
            sleep(.75)
            print(f"Here is your output matrix -->")
            
            print_matrix(masked_matrix)
            
            count += 1
        summary(option)
    else:
        return 0

def main():
    option = initiate_program()
    start_application(option)

if __name__ == "__main__":
    main()