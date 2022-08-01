'''
Attempt one: 29072022: Trying to come up with a naive approach to the problem
Rules to this solution:
1. For this attempt, we will not dwell deep into optimisation. 
2. I will use a sample list of list to build a matrix for the problem statement.
Basic background: the output can be returned in a separate memory space or can be achieved by in-place operation. 
Case 1:approach by utilising extra memory
'''

#helper function to print matrices
from time import sleep

def input_matrix(option):
    if option == 1:
        matrix = [[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
    elif option == 2:
        matrix = [[0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0], [0, 1, 0, 0, 1, 0], [0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0]]
    return matrix

def print_array(matrix):
    for idx in range(len(matrix)):
        print(matrix[idx])
    print()

# helper function to count elements
def count_elements(matrix):
    m, n = len(matrix), len(matrix[0]);
    input_zeroes, input_ones = 0, 0;
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                input_ones += 1;
            else:
                input_zeroes += 1;
    return [input_ones, input_zeroes]

#main function
def naive_solution(matrix):
    output_matrix = [[] for i in range(len(matrix))]

    m, n = len(matrix), len(matrix[0]);
    input_zeroes, input_ones = 0, 0;
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

    print(f"Here is your label state matrix -->") # adding to compare the previous state
    print_array(output_matrix)

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

if __name__ == "__main__":
    # number of rows in the matrix
    print(f"Welcome to the Game of Life CLI Application")
    sleep(2);1
    print(f"Here is the list of patterns, you can generate: \n1. Block \n2. Bee-Hive \n3. Blinker \n4. Toad \n5. Glider")
    print(f"To select the pattern you want to generate, type the option number from the list shown above");
    option = int(input());
    # print(f"Please enter the number of rows in the input matrix")
    # N = int(input()); 
    
    matrix = input_matrix(option);
    for idx in range(len(matrix)):
        print(matrix[idx])
    print()

    output_matrix = naive_solution(matrix);
    print(f"Here is your output matrix -->")
    print_array(output_matrix)

    # print(f"Summary: In the input array of dimension {N} X {len(matrix[0])}, there are {count_elements(matrix)[0]} 1s and {count_elements(matrix)[1]} 0s \nand the output array is of dimension {len(output_matrix)} X {len(output_matrix[0])} and the total number of {count_elements(output_matrix)[0]} 1s and {count_elements(output_matrix)[1]} 0s")