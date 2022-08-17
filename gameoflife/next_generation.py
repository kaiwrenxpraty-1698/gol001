from gameoflife.constants import ALIVE, DEAD


def next_generation_of(matrix):
    matrix_of_alive_neighbour_counts = _compute_number_of_living_neighbours_for(matrix)
    output_matrix = [row[:] for row in matrix]
    rows, columns = len(matrix), len(matrix[0])

    for row in range(rows):
        for column in range(columns):
            if matrix[row][column] == ALIVE:
                if matrix_of_alive_neighbour_counts[row][column] == 2 or \
                        matrix_of_alive_neighbour_counts[row][column] == 3:
                    output_matrix[row][column] = ALIVE
                else:
                    output_matrix[row][column] = DEAD
            else:
                if matrix_of_alive_neighbour_counts[row][column] == 3:
                    output_matrix[row][column] = ALIVE
                else:
                    output_matrix[row][column] = DEAD
    return output_matrix


def _compute_number_of_living_neighbours_for(matrix):
    living_cell_count_matrix = [[] for _ in range(len(matrix))]
    rows, columns = len(matrix), len(matrix[0])
    for row in range(rows):
        for column in range(columns):
            living_cell_count = 0
            for x in _neighbours_positions_for(row, rows):
                for y in _neighbours_positions_for(column, columns):
                    if _is_looking_outside_the_matrix_boundary(column, row, x, y):
                        continue
                    living_cell_count += matrix[x][y] % 2
            living_cell_count_matrix[row].append(living_cell_count)
    return living_cell_count_matrix


def _is_looking_outside_the_matrix_boundary(column, row, x, y):
    return x == row and y == column


def _neighbours_positions_for(row, rows):
    return range(max(row - 1, 0), min(row + 2, rows))
