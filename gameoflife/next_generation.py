'''
submodule with core game of life logic
'''
from gameoflife.constants import ALIVE, DEAD

class NextGeneration:
    '''
    class with core game of life logic
    '''
    def __init__(self, matrix):
        self.matrix = matrix

    def get_rows(self):
        '''
        method to access rows
        '''
        return len(self.matrix)
    
    def get_columns(self):
        '''
        method to access columns
        '''
        return len(self.matrix[0])

    def next_generation_of(self):
        '''
        core method of the game of life automata
        '''
        output_matrix = [row[:] for row in self.matrix]
        rows, columns = self.get_rows(), self.get_columns()

        for row in range(rows):
            for column in range(columns):
                output_matrix[row][column] = self._apply_the_rules_to_cell_at()
        return output_matrix

    def _compute_number_of_living_neighbours_for(self):
        living_cell_count_matrix = [[] for _ in range(len(self.matrix))]
        rows, columns = self.get_rows(), self.get_columns()
        for row in range(rows):
            for column in range(columns):
                living_cell_count = 0
                for x in self._neighbours_positions_for(row):
                    for y in self._neighbours_positions_for(column):
                        if self._is_looking_outside_the_matrix_boundary(column, row, x, y):
                            continue
                        living_cell_count += self.matrix[x][y] % 2
                living_cell_count_matrix[row].append(living_cell_count)
        return living_cell_count_matrix

    def _apply_the_rules_to_cell_at(self):
        if self.matrix[self.get_rows()][self.get_columns()] == ALIVE:
            return self._any_live_cell_with_two_or_more_neighbours_survives()
        else:
            return self._any_dead_cell_with_exactly_three_live_neighbours_becomes_a_live_cell()

    def _any_dead_cell_with_exactly_three_live_neighbours_becomes_a_live_cell(self):
        return ALIVE if self._compute_number_of_living_neighbours_for()[self.get_rows()][self.get_columns()] == 3 else DEAD

    def _any_live_cell_with_two_or_more_neighbours_survives(self):
        if self._compute_number_of_living_neighbours_for()[self.get_rows()][self.get_columns()] == 2 or self._compute_number_of_living_neighbours_for()[self.get_rows()][self.get_columns()] == 3:
            return ALIVE
        else:
            return DEAD

    def _is_looking_outside_the_matrix_boundary(self, column, row, x, y):
        return x == row and y == column

    def _neighbours_positions_for(self, row):
        return range(max(row - 1, 0), min(row + 2, self.get_rows()))