from gameoflife.constants import ALIVE, DEAD


def next_generation_of(matrix):
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
            if matrix[row][column] == ALIVE:
                if output_matrix[row][column] == 2 or output_matrix[row][column] == 3:
                    output_matrix[row][column] = ALIVE
                else:
                    output_matrix[row][column] = DEAD
            else:
                if output_matrix[row][column] == 3:
                    output_matrix[row][column] = ALIVE
                else:
                    output_matrix[row][column] = DEAD
                    
    return output_matrix
