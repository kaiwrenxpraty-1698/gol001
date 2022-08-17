def select_menu_option(option):
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
 