# John Conway's Game of Life
This is a small project that I put together in `Python3`. It is a simulation of [John Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life). This 'Game of Life' is a simple grid system containing 'active' and 'non-active' squares that evovle according to a specific set of rules:
1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

With the help of [Matplotlib](https://matplotlib.org) and [Numpy](https://numpy.org) I was able to create a simple simulation of this game.

By [Carlo Jacobs](http://carlojacobs.ga)

## Requirements
In order to run this program, you have to have the following installed on your computer.
1. [Python3](https://www.python.org)
1. [Matplotlib](https://matplotlib.org)
2. [Numpy](https://numpy.org)
Run the program by running: `python3 gol.py`.
