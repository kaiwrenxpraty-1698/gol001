from gameoflife.constants import ALIVE, DEAD


def next_generation_of(matrix):
    matrix_of_alive_neighbour_counts = _compute_number_of_living_neighbours_for(matrix)
    output_matrix = [row[:] for row in matrix]
    rows, columns = len(matrix), len(matrix[0])

    for row in range(rows):
        for column in range(columns):
            output_matrix[row][column] = _apply_the_rules_to_cell_at(row, column, matrix,
                                                                     matrix_of_alive_neighbour_counts)
    return output_matrix


def _apply_the_rules_to_cell_at(row, column, matrix, matrix_of_alive_neighbour_counts):
    if matrix[row][column] == ALIVE:
        return _any_live_cell_with_two_or_more_neighbours_survives(row, column,
                                                                   matrix_of_alive_neighbour_counts)
    else:
        return _any_dead_cell_with_exactly_three_live_neighbours_becomes_a_live_cell(row,
                                                                                     column,
                                                                                     matrix_of_alive_neighbour_counts)


def _any_dead_cell_with_exactly_three_live_neighbours_becomes_a_live_cell(row, column,
                                                                          matrix_of_alive_neighbour_counts):
    return ALIVE if matrix_of_alive_neighbour_counts[row][column] == 3 else DEAD


def _any_live_cell_with_two_or_more_neighbours_survives(row, column, matrix_of_alive_neighbour_counts):
    if matrix_of_alive_neighbour_counts[row][column] == 2 or matrix_of_alive_neighbour_counts[row][column] == 3:
        return ALIVE
    else:
        return DEAD


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
