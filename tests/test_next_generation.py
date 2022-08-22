import unittest

from gameoflife.constants import ALIVE, DEAD
from gameoflife.next_generation import NextGeneration


class TestApplication(unittest.TestCase):
    def test_implement_game_of_life(self):
        input_matrix = [
                           [DEAD, ALIVE, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
                           [DEAD, DEAD, ALIVE, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
                           [ALIVE, ALIVE, ALIVE, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD]
                       ] + [[0 for _ in range(10)] for _ in range(7)]

        expected_output_matrix = [
                                     [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
                                     [ALIVE, DEAD, ALIVE, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
                                     [DEAD, ALIVE, ALIVE, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
                                     [DEAD, ALIVE, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD]
                                 ] + [[0 for _ in range(10)] for _ in range(6)]

        self.assertEqual(NextGeneration(input_matrix).next_generation_of(), expected_output_matrix)

    def test_vertical_blinker_becomes_horizontal_in_next_generation(self):
        input_matrix = [
            [DEAD, DEAD, DEAD, DEAD, DEAD],
            [DEAD, DEAD, ALIVE, DEAD, DEAD],
            [DEAD, DEAD, ALIVE, DEAD, DEAD],
            [DEAD, DEAD, ALIVE, DEAD, DEAD],
            [DEAD, DEAD, DEAD, DEAD, DEAD]
        ]
        expected_output_matrix = [
            [DEAD, DEAD, DEAD, DEAD, DEAD],
            [DEAD, DEAD, DEAD, DEAD, DEAD],
            [DEAD, ALIVE, ALIVE, ALIVE, DEAD],
            [DEAD, DEAD, DEAD, DEAD, DEAD],
            [DEAD, DEAD, DEAD, DEAD, DEAD]
        ]

        self.assertEqual(NextGeneration(input_matrix).next_generation_of(), expected_output_matrix)

    def test_horizontal_blinker_becomes_vertical_in_next_generation(self):
        input_matrix = [
            [DEAD, DEAD, DEAD, DEAD, DEAD],
            [DEAD, DEAD, DEAD, DEAD, DEAD],
            [DEAD, ALIVE, ALIVE, ALIVE, DEAD],
            [DEAD, DEAD, DEAD, DEAD, DEAD],
            [DEAD, DEAD, DEAD, DEAD, DEAD]
        ]
        expected_output_matrix = [
            [DEAD, DEAD, DEAD, DEAD, DEAD],
            [DEAD, DEAD, ALIVE, DEAD, DEAD],
            [DEAD, DEAD, ALIVE, DEAD, DEAD],
            [DEAD, DEAD, ALIVE, DEAD, DEAD],
            [DEAD, DEAD, DEAD, DEAD, DEAD]
        ]

        self.assertEqual(NextGeneration(input_matrix).next_generation_of(), expected_output_matrix)

    def test_block_remains_unchanged_in_next_generation(self):
        input_matrix = [
            [DEAD, DEAD, DEAD, DEAD, DEAD],
            [DEAD, DEAD, DEAD, DEAD, DEAD],
            [DEAD, ALIVE, ALIVE, DEAD, DEAD],
            [DEAD, ALIVE, ALIVE, DEAD, DEAD],
            [DEAD, DEAD, DEAD, DEAD, DEAD]
        ]
        expected_output_matrix = [row[:] for row in input_matrix]

        self.assertEqual(NextGeneration(input_matrix).next_generation_of(), expected_output_matrix)


if __name__ == "__main__":
    unittest.main()
