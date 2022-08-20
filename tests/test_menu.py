import unittest

from gameoflife.constants import DEAD, ALIVE
from gameoflife.menu import select_menu_option


class TestSelectInputMatrix(unittest.TestCase):
    def test_select_from_matrix_option(self):
        option = "5"
        expected_output_matrix = [[DEAD, ALIVE, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
                                  [DEAD, DEAD, ALIVE, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
                                  [ALIVE, ALIVE, ALIVE, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD]
                                  ] + [[DEAD for _ in range(10)] for _ in range(7)]

        self.assertEqual(select_menu_option(option), expected_output_matrix)


if __name__ == "__main__":
    unittest.main()
