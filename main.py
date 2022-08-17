'''
Context:
This code will display standard examples of Game of Life, based on the option selected
'''
from time import sleep
import sys
import json

with open('assets/input.json') as f:
    summary_dict = json.load(f)

def summary(option):
        print(summary_dict[option])
    
def introduction(option):
    name_of_pattern = summary_dict['mapping'][option]
    print(f'Welcome to the Game of Life; So glad that you have chosen {name_of_pattern}')

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


def select_from_matrix_option(option):
    live_cell, dead_cell = 1, 0
    if option == "1":
        matrix = [
            [dead_cell, dead_cell, dead_cell, dead_cell], 
            [dead_cell, live_cell, live_cell, dead_cell], 
            [dead_cell, live_cell, live_cell, dead_cell], 
            [dead_cell, dead_cell, dead_cell, dead_cell]
            ]
    elif option == "2":
        matrix = [
            [dead_cell, dead_cell, dead_cell, dead_cell, dead_cell, dead_cell], 
            [dead_cell, dead_cell, live_cell, live_cell, dead_cell, dead_cell], 
            [dead_cell, live_cell, dead_cell, dead_cell, live_cell, dead_cell], 
            [dead_cell, dead_cell, live_cell, live_cell, dead_cell, dead_cell], 
            [dead_cell, dead_cell, dead_cell, dead_cell, dead_cell, dead_cell]
            ]
    elif option == "3":
        matrix = [
            [dead_cell, dead_cell, dead_cell, dead_cell, dead_cell], 
            [dead_cell, dead_cell, live_cell, dead_cell, dead_cell], 
            [dead_cell, dead_cell, live_cell, dead_cell, dead_cell], 
            [dead_cell, dead_cell, live_cell, dead_cell, dead_cell], 
            [dead_cell, dead_cell, dead_cell, dead_cell, dead_cell]
            ]
    elif option == "4":
        matrix = [
            [dead_cell, dead_cell, dead_cell, dead_cell, dead_cell, dead_cell], 
            [dead_cell, dead_cell, dead_cell, live_cell, dead_cell, dead_cell], 
            [dead_cell, live_cell, dead_cell, dead_cell, live_cell, dead_cell], 
            [dead_cell, live_cell, dead_cell, dead_cell, live_cell, dead_cell], 
            [dead_cell, dead_cell, live_cell, dead_cell, dead_cell, dead_cell], 
            [dead_cell, dead_cell, dead_cell, dead_cell, dead_cell, dead_cell]
            ]
    elif option == "5":
        matrix = [
            [dead_cell, live_cell, dead_cell, dead_cell, dead_cell, dead_cell, dead_cell, dead_cell, dead_cell, dead_cell], 
            [dead_cell, dead_cell, live_cell, dead_cell, dead_cell, dead_cell, dead_cell, dead_cell, dead_cell, dead_cell], 
            [live_cell, live_cell, live_cell, dead_cell, dead_cell, dead_cell, dead_cell, dead_cell, dead_cell, dead_cell]
            ] + [[dead_cell for _ in range(10)] for _ in range(7)]
    else:
        exit()
    return matrix
                
def implement_game_of_life(matrix):
    output_matrix = [[] for _ in range(len(matrix))]
    rows, columns = len(matrix), len(matrix[0])
    for row in range(rows):
        for column in range(columns):
            living_cells = 0
            for x in range(max(row - 1, 0), min(row + 2, rows)):
                for y in range(max(column - 1, 0), min(column + 2, columns)):
                    if x == row and y == column:
                        continue
                    living_cells += matrix[x][y] % 2        
            output_matrix[row].append(living_cells)

    for row in range(rows):
        for column in range(columns):
            if matrix[row][column] == 1:
                if output_matrix[row][column] == 2 or output_matrix[row][column] == 3:
                    output_matrix[row][column] = 1   
                else:
                    output_matrix[row][column] = 0
            else:
                if output_matrix[row][column] == 3:
                    output_matrix[row][column] = 1
                else:
                    output_matrix[row][column] = 0
                    
    return output_matrix

def start_application(option):
    if option == "1" or option == "2":
        introduction(option)
        matrix = select_from_matrix_option(option)
        matrix = implement_game_of_life(matrix)
        print(f"Here is your output matrix -->")
        print_matrix(mask_input_matrix(matrix))
        summary(option)    
    elif option == "3" or option == "4":
        matrix = select_from_matrix_option(option)
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

def main():
    try:
        option = sys.argv[1]
    except IndexError:
        option = "null"

    start_application(option)

if __name__ == "__main__":
    main()