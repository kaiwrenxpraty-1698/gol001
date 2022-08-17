'''
Context:
This code will display standard examples of Game of Life, based on the option selected
'''
from time import sleep
import sys
import sample.core, sample.select_input_matrix, sample.helper
               
def start_application(option):
    if option == "1" or option == "2":
        sample.helper.introduction(option)
        matrix = sample.select_input_matrix.select_from_matrix_option(option)
        matrix = sample.core.implement_game_of_life(matrix)
        print(f"Here is your output matrix -->")
        sample.helper.print_matrix(sample.helper.mask_input_matrix(matrix))
        sample.helper.summary(option)    
    elif option == "3" or option == "4":
        matrix = sample.select_input_matrix.select_from_matrix_option(option)
        count = 0
        while count < 10:
            matrix = sample.core.implement_game_of_life(matrix)
            sleep(.5)
            print(f"Here is your output matrix -->")
            sample.helper.print_matrix(sample.helper.mask_input_matrix(matrix))
            print(f"State of the matrix --> {count%2}")
            count += 1
        sample.helper.summary(option)
    elif option == "5":
        matrix = sample.select_input_matrix.select_from_matrix_option(option)
        count = 0
        while count < 25:
            matrix = sample.core.implement_game_of_life(matrix)
            sleep(.75)
            print(f"Here is your output matrix -->")
            sample.helper.print_matrix(sample.helper.mask_input_matrix(matrix))
            count += 1
        sample.helper.summary(option)
    elif option == "help":
        print(sample.helper.summary_dict['help'])
        return 0
    else:
        print(sample.helper.summary_dict['error'])
        return 0

def main():
    try:
        option = sys.argv[1]
    except IndexError:
        option = "null"

    start_application(option)

if __name__ == "__main__":
    main()