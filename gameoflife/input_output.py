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
