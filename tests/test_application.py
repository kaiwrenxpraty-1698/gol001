import unittest

from gameoflife.core import implement_game_of_life


class TestApplication(unittest.TestCase):
    def test_implement_game_of_life(self):
        input_matrix = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
                        ] + [[0 for _ in range(10)] for _ in range(7)]

        expected_output_matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]] + [[0 for _ in range(10)] for _ in range(6)]

        self.assertEqual(implement_game_of_life(input_matrix), expected_output_matrix)


if __name__ == "__main__":
    unittest.main()
