'''
Context:
This code will display standard examples of Game of Life, based on the option selected
'''
from time import sleep
import argparse

arg_desc = '''\
    'Welcome to the Game of Life. 
    Please select the option number corresponding to the pattern, you will like to print: 
    1. Block 
    2. Bee-Hive 
    3. Blinker 
    4. Toad 
    5. Glider
'''


def initiate_program():
    parser = argparse.ArgumentParser(formatter_class = argparse.RawDescriptionHelpFormatter, description = arg_desc)
    parser.add_argument('-o', '--option', type = int, metavar = '', required = True, help = f'Option corresponding to the pattern in the help description')
    args = parser.parse_args()

    option = args.option
    matrix = select_matrix_option(option)
    new_matrix = mask_input_matrix(matrix)
    print(f"Holla! You have chosen option number {option}, this is the initial state of the grid -->")
    print()
    print_matrix(new_matrix)
    sleep(.75)
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
                output_matrix[idx].append("A")
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


def show_matrix(matrix):
    for idx in range(len(matrix)):
            print(matrix[idx])


def start_application(option, matrix):
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

    if option == 1 or option == 2:
        output_matrix = implement_game_of_life(matrix)
        masked_matrix = mask_input_matrix(output_matrix)
        print(f"Here is your output matrix -->");
        print();
        show_matrix(masked_matrix);
        print();
        summary(option)    
    elif option == 3 or option == 4:
        count = 0;
        while count < 10:
            matrix = implement_game_of_life(matrix);
            masked_matrix = mask_input_matrix(matrix);
            sleep(.5)
            print(f"Here is your output matrix -->");
            print();
            show_matrix(masked_matrix);
            print();
            print(f"State of the matrix --> {count%2}")
            count += 1;
            print();
        summary(option);
    elif option == 5:
        count = 0;
        while count < 25:
            matrix = implement_game_of_life(matrix);
            masked_matrix = mask_input_matrix(matrix);
            sleep(.75)
            print(f"Here is your output matrix -->");
            print();
            show_matrix(masked_matrix);
            print();
            count += 1;
        summary(option);
    else:
        return 0


def main():
    option, matrix = initiate_program();
    start_application(option, matrix);


if __name__ == "__main__":
    main()