import unittest

from gameoflife.select_input_matrix import select_from_matrix_option


class TestSelectInputMatrix(unittest.TestCase):
    def test_select_from_matrix_option(self):
        option = "5"
        expected_output_matrix = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                               [1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
                               ] + [[0 for _ in range(10)] for _ in range(7)]

        self.assertEqual(select_from_matrix_option(option), expected_output_matrix)


if __name__ == "__main__":
    unittest.main()
