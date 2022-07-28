# Conway's Game of Life

## Objective of this repo

### What is Conway's Game of Life?

[Sourced from Wikipedia] (/https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)

Disclaimer: I am adding the what I understand from the wiki article over here.

1. The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, live or dead (or populated and unpopulated, respectively). 

Explanation: In pure programming terms, from an execution lens, this is a 2D Matrix problem where we can denote the live state, by 1 and the dead state by 0 and construct a Matrix and implement the logic.

2. Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent.

2. 1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2. 2. Any live cell with two or three live neighbours lives on to the next generation.
2. 3. Any live cell with more than three live neighbours dies, as if by overpopulation.
2. 4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

Explanation: This is the the logic that we need to implement in order to generate the the final state for the 2D Matrix.
