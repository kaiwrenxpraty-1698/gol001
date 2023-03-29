import unittest

from gameoflife.constants import DEAD, ALIVE
from gameoflife.input_output import InputOutput


class TestInputOutput(unittest.TestCase):
    def test_select_from_matrix_option(self):
        option = "5"
        expected_output_matrix = [
            [DEAD, ALIVE, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
            [DEAD, DEAD, ALIVE, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
            [ALIVE, ALIVE, ALIVE, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
        ] + [[DEAD for _ in range(10)] for _ in range(7)]

        self.assertEqual(
            InputOutput(option, None).select_menu_option(), expected_output_matrix
        )


if __name__ == "__main__":
    unittest.main()
