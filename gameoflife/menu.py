from gameoflife.constants import DEAD, ALIVE, BLOCK_PATTERN


class Menu:
    menu_options = {
        "1": BLOCK_PATTERN,
        "2": [
            [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
            [DEAD, DEAD, ALIVE, ALIVE, DEAD, DEAD],
            [DEAD, ALIVE, DEAD, DEAD, ALIVE, DEAD],
            [DEAD, DEAD, ALIVE, ALIVE, DEAD, DEAD],
            [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD]
        ],
        "3": [
            [DEAD, DEAD, DEAD, DEAD, DEAD],
            [DEAD, DEAD, ALIVE, DEAD, DEAD],
            [DEAD, DEAD, ALIVE, DEAD, DEAD],
            [DEAD, DEAD, ALIVE, DEAD, DEAD],
            [DEAD, DEAD, DEAD, DEAD, DEAD]
        ],
        "4": [
            [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
            [DEAD, DEAD, DEAD, ALIVE, DEAD, DEAD],
            [DEAD, ALIVE, DEAD, DEAD, ALIVE, DEAD],
            [DEAD, ALIVE, DEAD, DEAD, ALIVE, DEAD],
            [DEAD, DEAD, ALIVE, DEAD, DEAD, DEAD],
            [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD]
        ],
        "5": [[DEAD, ALIVE, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
              [DEAD, DEAD, ALIVE, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
              [ALIVE, ALIVE, ALIVE, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD]
              ] + [[DEAD for _ in range(10)] for _ in range(7)]
    }

    def __init__(self, option):
        self.option = option

    def grid_for_option(self):
        return self.menu_options[self.option]

    def is_valid_option(self):
        return self.option in self.menu_options.keys()
