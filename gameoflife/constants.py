ALIVE = 1
DEAD = 0

BLOCK_PATTERN = [
    [DEAD, DEAD, DEAD, DEAD],
    [DEAD, ALIVE, ALIVE, DEAD],
    [DEAD, ALIVE, ALIVE, DEAD],
    [DEAD, DEAD, DEAD, DEAD]
]

SUMMARY_DICT = {
    "1" :"This is the most common still life pattern of Game of Life: Block. \nKey point: the state of matrix is identical to the input matrix.",
    "2":"This is the another common still life pattern of Game of Life: Bee-hive. \nKey point: the state of matrix is identical to the input matrix.",
    "3":"This is a popular oscillator pattern of Game of Life: Blinker. \nKey point: the matrix reaches its initial state after exactly 2 iterations, hence the pattern keeps oscillating.",
    "4":"This is a popular oscillator pattern of Game of Life: Toad. \nKey point: the matrix reaches its initial state after exactly 2 iterations, hence the pattern keeps oscillating.",
    "5":"This is the most popular Spaceships pattern of Game of Life: Glider. \nKey point: the pattern keeps gliding over the matrix",
    "help": "Welcome to the Game of Life.\nPlease select the option number corresponding to the pattern, you will like to print: \n1. Block \n2. Bee-Hive \n3. Blinker \n4. Toad \n5. Glider",
    "error":"Sorry this option is not valid, please add help argument to know how the tool works",
    "mapping":{
        "1": "Block",
        "2": "Bee-Hive",
        "3": "Blinker",
        "4": "Toad",
        "5": "Glider"
}
}