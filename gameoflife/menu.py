from gameoflife.constants import DEAD, ALIVE


def select_menu_option(option):
    if option == "1":
        matrix = [
            [DEAD, DEAD, DEAD, DEAD], 
            [DEAD, ALIVE, ALIVE, DEAD], 
            [DEAD, ALIVE, ALIVE, DEAD], 
            [DEAD, DEAD, DEAD, DEAD]
            ]
    elif option == "2":
        matrix = [
            [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD], 
            [DEAD, DEAD, ALIVE, ALIVE, DEAD, DEAD], 
            [DEAD, ALIVE, DEAD, DEAD, ALIVE, DEAD], 
            [DEAD, DEAD, ALIVE, ALIVE, DEAD, DEAD], 
            [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD]
            ]
    elif option == "3":
        matrix = [
            [DEAD, DEAD, DEAD, DEAD, DEAD], 
            [DEAD, DEAD, ALIVE, DEAD, DEAD], 
            [DEAD, DEAD, ALIVE, DEAD, DEAD], 
            [DEAD, DEAD, ALIVE, DEAD, DEAD], 
            [DEAD, DEAD, DEAD, DEAD, DEAD]
            ]
    elif option == "4":
        matrix = [
            [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD], 
            [DEAD, DEAD, DEAD, ALIVE, DEAD, DEAD], 
            [DEAD, ALIVE, DEAD, DEAD, ALIVE, DEAD], 
            [DEAD, ALIVE, DEAD, DEAD, ALIVE, DEAD], 
            [DEAD, DEAD, ALIVE, DEAD, DEAD, DEAD], 
            [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD]
            ]
    elif option == "5":
        matrix = [
            [DEAD, ALIVE, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD], 
            [DEAD, DEAD, ALIVE, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD], 
            [ALIVE, ALIVE, ALIVE, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD]
            ] + [[DEAD for _ in range(10)] for _ in range(7)]
    else:
        exit()
    return matrix
 