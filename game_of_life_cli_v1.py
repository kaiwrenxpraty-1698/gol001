'''
Attempt one: 29072022: Trying to come up with a naive approach to the problem
Rules to this solution:
1. For this attempt, we will not dwell deep into optimisation. 
2. I will use a sample list of list to build a matrix for the problem statement.
Basic background: the output can be returned in a separate memory space or can be achieved by in-place operation. 
Case 1:approach by utilising extra memory
'''
import os
#helper function to print matrices
from time import sleep

def starter_function():
    print(f"Welcome to the Game of Life CLI Application");
    sleep(.5);
    print(f"Here is the list of patterns, you can generate: \n1. Block \n2. Bee-Hive \n3. Blinker \n4. Toad \n5. Glider");
    print(f"To select the pattern you want to generate, type the option number from the list shown above -->");
    option = int(input());
    print(f"Here is your input matrix -->");

    return option

def input_matrix(option):
    if option == 1:
        matrix = [[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]];
    elif option == 2:
        matrix = [[0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0], [0, 1, 0, 0, 1, 0], [0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0]];
    elif option == 3:
        matrix = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]];
    elif option == 4:
        matrix = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 1, 0], [0, 1, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0]];
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
# Adding driver function to animate Cases 3 & 4 from our SE Log Standard Examples:
def driver_function(option, matrix):
    def summary(option): #helper function to print summaries
        if option == 1:
            print(f"This is the most common still life pattern of Game of Life: Block \nThe state of matrix is identical to the input matrix");
        elif option == 2:
            print(f"This is the another common still life pattern of Game of Life: Bee-hive \nThe state of matrix is identical to the input matrix");
        elif option == 3:
            print(f"This is a popular oscillator pattern of Game of Life: Blinker \nThe matrix reaches its initial state after exactly 2 iterations, \nhence the pattern keeps repeating itself");
        elif option == 4:
            print(f"This is a popular oscillator pattern of Game of Life: Toad \nThe matrix reaches its initial state after exactly 2 iterations, \nhence the pattern keeps repeating itself");


    if option == 1 or option == 2:
        output_matrix = naive_solution(matrix);
        print(f"Here is your output matrix -->");
        print_array(output_matrix);
        summary(option)
        
    elif option == 3 or option == 4:
        count = 0;
        while count < 10:
            matrix = naive_solution(matrix);
            sleep(.5)
            print(f"Here is your output matrix -->");
            print_array(matrix);
            count += 1;
            print(f"State of the matrix --> {count}")
        summary(option)

        

if __name__ == "__main__":
    option = starter_function();

    matrix = input_matrix(option);
    print_array(matrix);
    driver_function(option, matrix);