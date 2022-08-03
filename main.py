'''
Attempt Two: 01082022: Trying to implement standard examples:
1. Block
2. Bee-Hive
3. Blinker
4. Toad
5. Glider

Main Objectives:
1. Implement the standard examples.
2. Improve the user experience for the end user
    2.1 Make the printed matrix more readble
    2.2 Provide clear instructions to the user for generating standard test cases.
3. Make the code far more functional
'''
from time import sleep

def initiate_program():
    print(f'Welcome to the Game of Life CLI Application')
    sleep(0.5)
    print(f"Here is the list of patterns, you can generate: \n1. Block \n2. Bee-Hive \n3. Blinker \n4. Toad \n5. Glider")

    print(f"To select the pattern you want to generate, type the option number from the list shown above -->")

    option = int(input())
    print(f"Here is your input matrix -->")
    print()
    matrix = select_matrix_option(option)
    new_matrix = mask_input_matrix(matrix)
    print_matrix(new_matrix)
    print()
    return option, matrix

def select_matrix_option(option):
    if option == 1:
        matrix = [[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
    elif option == 2:
        matrix = [[0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0], [0, 1, 0, 0, 1, 0], [0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0]]
    elif option == 3:
        matrix = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
    elif option == 4:
        matrix = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 1, 0], [0, 1, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    elif option == 5:
        matrix = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 0, 0, 0, 0]] + [[0 for _ in range(10)] for _ in range(7)]
    else:
        print(f"Sorry! Invalid input")
        print()
        exit();
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
                output_matrix[idx].append("A")
    return output_matrix
                

def implement_game_of_life(matrix):
    output_matrix = [[] for _ in range(len(matrix))]
    m, n = len(matrix), len(matrix[0])
    input_zeroes, input_ones = 0, 0;
    for i in range(m):
        for j in range(n):
            living_cells = 0;
            for x in range(max(i - 1, 0), min(i + 2, m)):
                for y in range(max(j - 1, 0), min(j + 2, n)):
                    if x == i and y == j: 
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

def driver_function(option, matrix):
    def summary(option):
        print()
        if option == 1:
            print(f"This is the most common still life pattern of Game of Life: Block; the state of matrix is identical to the input matrix.")
        elif option == 2:
            print(f"This is the another common still life pattern of Game of Life: Bee-hive; the state of matrix is identical to the input matrix.")
        elif option == 3:
            print(f"This is a popular oscillator pattern of Game of Life: Blinker; the matrix reaches its initial state after exactly 2 iterations, hence the pattern keeps oscillating.");
        elif option == 4:
            print(f"This is a popular oscillator pattern of Game of Life: Toad; the matrix reaches its initial state after exactly 2 iterations, hence the pattern keeps oscillating.");  
        elif option == 5:
             print(f"This is the most popular Spaceships pattern of Game of Life: Glider; the pattern keeps gliding over the matrix"); 
        else:
            return 0
        print()

    if option == [1,2]:
        output_matrix = implement_game_of_life(matrix)
        print_matrix = mask_input_matrix(output_matrix)
        print(f"Here is your output matrix -->");
        print();
        print_matrix(print_matrix);
        print();
        summary(option)
        
    elif option == [3,4]:
        count = 0;
        while count < 10:
            matrix = implement_game_of_life(matrix);
            print_matrix = mask_input_matrix(matrix);
            sleep(.5)
            print(f"Here is your output matrix -->");
            print();
            print_matrix(print_matrix);
            print();
            print(f"State of the matrix --> {count%2}")
            count += 1;
            print();
        summary(option);
    elif option == 5:
        count = 0;
        while count < 25:
            matrix = implement_game_of_life(matrix);
            print_matrix = mask_input_matrix(matrix);
            sleep(.75)
            print(f"Here is your output matrix -->");
            print();
            print_matrix(print_matrix);
            print();
            count += 1;
        summary(option);
    else:
        return 0


if __name__ == "__main__":
    option, matrix = initiate_program();
    driver_function(option, matrix);