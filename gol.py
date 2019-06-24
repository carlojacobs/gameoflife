# Game of life
# Imports
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Grid:

    """Grid class"""

    def __init__(self, x_size, y_size, initial_state):
        """Initialize the Grid class"""
        self.x_size = x_size
        self.y_size = y_size
        self.initial_state = initial_state
        self.cells = []
        self.initialize_cells()

    def initialize_cells(self):
        """Initialize the cells in the grid"""
        for row in range(self.y_size):
            for column in range(self.x_size):
                new_cell_state = False
                location_array = [column, row]
                for state in self.initial_state:
                    if state == location_array:
                        new_cell_state = True
                new_cell = Cell(column, row, new_cell_state)
                self.add_cell(new_cell)

    def add_cell(self, cell):
        """Add a cell to the grid"""
        self.cells.append(cell)

    def get_alive_cells(self):
        """Get an array with the alive cells"""
        alive_cells = []
        for cell in self.cells:
            if cell.alive:
                alive_cells.append(cell)
        return alive_cells

    def update_cells(self):
        """Update the cell status based on the number of neighbours"""
        for i in range(0, len(self.cells)):
            cell = self.cells[i]
            neighbours = cell.get_neighbours(self.cells)
            if cell.alive:
                if neighbours < 2:
                    self.cells[i].alive = False
                elif neighbours > 3:
                    self.cells[i].alive = False
            else:
                if neighbours == 3:
                    self.cells[i].alive = True

class Cell:

    """Cell class"""

    def __init__(self, x, y, alive):
        """Initialize cell class"""
        self.x = x
        self.y = y
        self.alive = alive
        self.num_neighbours = 0

    def compute_distance(self, x1, y1, x2, y2):
        """Compute the distance between two cells"""
        return np.sqrt((x1-x2)**2 + (y1-y2)**2)

    def get_neighbours(self, cells):
        """Get the number of neihbours of a cell"""
        neighbours = 0
        for cell in cells:
            distance = self.compute_distance(self.x, self.y, cell.x, cell.y)
            if (int(distance) == 1 or distance == np.sqrt(2)) and cell.alive:
                neighbours += 1
        return neighbours 

class Game:

    """Game class"""

    def __init__(self, x_size, y_size, live_cells):
        """Initialize game class"""
        self.initial_states = self.generate_initial_states(x_size, y_size, live_cells)
        self.grid = Grid(x_size, y_size, self.initial_states)

    def generate_initial_states(self, x_size, y_size, num):
        """Generate a random initial grid state"""
        states = []
        for i in range(num):
            random_state = [np.random.randint(x_size), np.random.randint(y_size)]
            states.append(random_state)
        return states

    def to_bits(self, n):
        """Convert the grid to a bit representation"""
        if n == True:
            return 1
        else:
            return 0

    def get_grid(self, grid):
        """Get the current state of the grid"""
        cells = self.grid.cells
        grid_state = [x.alive for x in cells]
        grid_state = list(map(self.to_bits, grid_state))
        grid_state = np.array(grid_state)
        grid_state = grid_state.reshape((self.grid.x_size, self.grid.y_size))
        return grid_state

    def clear(self):
        """Clear the console"""
        os.system('clear')

    def run_game(self):
        """Run the game in the console"""
        while True:
            self.clear()
            print(self.get_grid(self.grid))
            self.grid.update_cells()

    def run_game_with_limit(self, limit):
        """Run the game in the console with an iteration limit"""
        i = 0
        while i < limit:
            self.clear()
            print(self.get_grid(self.grid))
            self.grid.update_cells()
            i += 1

def animate(i):
    """Animate the game using matplotlib"""
    game.grid.update_cells()
    matrix = game.get_grid(game.grid)
    ax1.clear()
    num_of_cells = str(len(game.grid.get_alive_cells()))
    cell_history.append(num_of_cells)
    ax1.set_title("Number of alive cells: " + num_of_cells)
    ax1.matshow(matrix, cmap="gray_r")

def animate_num_of_cells(i):
    """Animate and plot the number of alive cells using matplotlib"""
    ax2.clear()
    ax2.plot(cell_history)

# Some global vars
cell_history = []
fig = plt.figure()
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

def start_game():
    """Initiate the game using user input"""
    y_size = int(input("Height of game: "))
    x_size = int(input("Width of game: "))
    cells = int(input(f"Number of alive cells (out of {x_size*y_size}): "))
    choice = input("Animation (A) or Command Line (B): ")
    global game
    game = Game(x_size, y_size, cells)
    if choice == "B":
    	game.run_game()
    elif choice == "A":
    	# Animation
    	ani1 = animation.FuncAnimation(fig, animate, interval=10)
    	ani2 = animation.FuncAnimation(fig, animate_num_of_cells, interval=10)
    	plt.show()
    else:
    	print("Please choose something else.")
    
if __name__ == "__main__":
    start_game()
