"""
submodule for Menu class
"""
from gameoflife.constants import DEAD, ALIVE, BLOCK_PATTERN


class Menu:
    """
    Class for input templates and generating matrix based on option input
    """

    menu_options = {
        "1": BLOCK_PATTERN,
        "2": [
            [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
            [DEAD, DEAD, ALIVE, ALIVE, DEAD, DEAD],
            [DEAD, ALIVE, DEAD, DEAD, ALIVE, DEAD],
            [DEAD, DEAD, ALIVE, ALIVE, DEAD, DEAD],
            [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
        ],
        "3": [
            [DEAD, DEAD, DEAD, DEAD, DEAD],
            [DEAD, DEAD, ALIVE, DEAD, DEAD],
            [DEAD, DEAD, ALIVE, DEAD, DEAD],
            [DEAD, DEAD, ALIVE, DEAD, DEAD],
            [DEAD, DEAD, DEAD, DEAD, DEAD],
        ],
        "4": [
            [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
            [DEAD, DEAD, DEAD, ALIVE, DEAD, DEAD],
            [DEAD, ALIVE, DEAD, DEAD, ALIVE, DEAD],
            [DEAD, ALIVE, DEAD, DEAD, ALIVE, DEAD],
            [DEAD, DEAD, ALIVE, DEAD, DEAD, DEAD],
            [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
        ],
        "5": [
            [DEAD, ALIVE, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
            [DEAD, DEAD, ALIVE, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
            [ALIVE, ALIVE, ALIVE, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
        ]
        + [[DEAD for _ in range(10)] for _ in range(7)],
    }

    def __init__(self, option):
        self.option = option

    def grid_for_option(self):
        """
        method to select input matrix template
        """
        return self.menu_options[self.option]

    def is_valid_option(self):
        """
        method to check valid input option
        """
        return self.option in self.menu_options.keys()
