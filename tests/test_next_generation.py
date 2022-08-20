import unittest

from gameoflife.constants import ALIVE, DEAD
from gameoflife.next_generation import next_generation_of


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

        self.assertEqual(next_generation_of(input_matrix), expected_output_matrix)


if __name__ == "__main__":
    unittest.main()
