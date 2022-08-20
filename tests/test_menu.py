import unittest

from gameoflife.constants import BLOCK_PATTERN
from gameoflife.menu import Menu


class TestMenu(unittest.TestCase):
    def test_menu_option_1_is_valid(self):
        self.assertEqual(Menu("1").is_valid_option(), True)

    def test_menu_option_2_is_valid(self):
        self.assertEqual(Menu("2").is_valid_option(), True)

    def test_menu_option_3_is_valid(self):
        self.assertEqual(Menu("3").is_valid_option(), True)

    def test_menu_option_4_is_valid(self):
        self.assertEqual(Menu("4").is_valid_option(), True)

    def test_menu_option_5_is_valid(self):
        self.assertEqual(Menu("5").is_valid_option(), True)

    def test_menu_option_6_is_not_valid(self):
        self.assertEqual(Menu("6").is_valid_option(), False)

    def test_menu_option_0_is_not_valid(self):
        self.assertEqual(Menu("0").is_valid_option(), False)

    def test_menu_option_One_is_not_valid(self):
        self.assertEqual(Menu("One").is_valid_option(), False)

    def test_menu_option_1_returns_block(self):
        self.assertEqual(Menu("1").grid_for_option(), BLOCK_PATTERN)

if __name__ == "__main__":
    unittest.main()
