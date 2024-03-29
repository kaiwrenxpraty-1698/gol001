# Conway's Game of Life

Python code to run a few standard examples of Conway's Game of Life

***

### Usage
Use the below command to know about the application and the how to use it.
```
python3 main.py help
```
Use the below command to run the application and display patterns for the chosen option

```
python3 main.py option_number
```
Replace option number with the number corresponding to the pattern in the `help` command.

Run the blinker example using
```
make blinker
```

Run tests using
```
make test
```

Coverage Report
```
Name                            Stmts   Miss  Cover
---------------------------------------------------
gameoflife/__init__.py              0      0   100%
gameoflife/constants.py             3      0   100%
gameoflife/input_output.py         32     15    53%
gameoflife/menu.py                  9      0   100%
gameoflife/next_generation.py      42      0   100%
tests/__init__.py                   0      0   100%
tests/test_input_output.py         10      1    90%
tests/test_menu.py                 24      1    96%
tests/test_next_generation.py      22      1    95%
---------------------------------------------------
TOTAL                             142     18    87%
```

***

### What is Conway's Game of Life?

#### Brief Introduction

The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970.[1] It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves. It is Turing complete and can simulate a universal constructor or any other Turing machine.

[For further understanding](/https://en.wikiedia.org/wiki/Conway%27s_Game_of_Life)

#### Key features of the algorithm
The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, live or dead (or populated and unpopulated, respectively). Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

These rules, which compare the behavior of the automaton to real life, can be condensed into the following:

1. Any live cell with two or three live neighbours survives.
2. Any dead cell with three live neighbours becomes a live cell.
3. All other live cells die in the next generation. Similarly, all other dead cells stay dead.