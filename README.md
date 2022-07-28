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


### Initial Execution Steps:

After going through the [SE Log](https://docs.google.com/document/d/1jIExgMhHwKZAXokPp7g4wO5mq7UYwO-M9sqCkTQf0Lk/edit#heading=h.n6urvrl4qa3l), here is how I am planning to approach this.

NOTE: This is based on the preliminary assessment, that I am making based on my understanding so far.
We have two broad sections to the problem statement.

1. Getting the logic right!
In this section, we will try to implement the algorithm.
As I have mentioned above, this is a 2D Matrix problem from a pure Data Structures & Algorithms perspective.

2. Building the CLI application.
This is an interesting part of the project which I will be trying out for the first time. Based on the intial assessment of the problem statement, here are the tools and libraries that I will be using.

1. argparser: python library to take input from the user through the console. 
2. Docker: to deliver the CLI application in form of individual containers.
