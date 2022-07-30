'''
Attempt one: 29072022: Trying to come up with a naive approach to the problem
Rules to this solution:
1. For this attempt, we will not dwell deep into optimisation. 
2. I will use a sample list of list to build a matrix for the problem statement.
'''

matrix = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]];

'''
Basic background: the output can be returned in a separate memory space or can be achieved by in-place operation. 
'''

#approach by utilising extra memory

import argparse
parser = argparse.ArgumentParser()

parser.add_argument("--matrix", type=[], required= True)

args = parser.parse_args()

matrix = args.matrix

def naive_solution(matrix):
    output_matrix = [[] for i in range(len(matrix))]

    m, n = len(matrix), len(matrix[0]);

    for i in range(m):
        for j in range(n):
            # we access the cells of the matrix
            # we will proceed to count the neighbours of each cell
            living_cells = 0;
            for x in range(max(i - 1, 0), min(i + 2, m)):
                for y in range(max(j - 1, 0), min(j + 2, n)):
                    if x == i and y == j: # if the scanning matrix matches the cell; it simply skips the scan
                        continue
                    living_cells += matrix[x][y] % 2;        
            output_matrix[i].append(living_cells)

    print(output_matrix) # adding to compare the previous state
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                if output_matrix[i][j] == 2 or output_matrix[i][j] == 3:
                    output_matrix[i][j] = 1;
                else:
                    output_matrix[i][j] = 0;
            else:
                if output_matrix[i][j] == 3:
                    output_matrix[i][j] = 1;
                else:
                    output_matrix[i][j] = 0;

    return output_matrix

print(naive_solution(matrix))