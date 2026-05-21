import random
import time
import os


# ============================================================
# Classe Cell
# ============================================================

class Cell:
    """A class to represent a single cell in the grid."""

    def __init__(self, alive=False):
        """Initialize a cell as alive or dead."""
        self.alive = alive

    def __str__(self):
        """Return a visual representation of the cell."""
        return "█" if self.alive else "·"


# ============================================================
# Classe Grid
# ============================================================

class Grid:
    """A class to represent the game grid."""

    def __init__(self, rows, cols):
        """Initialize the grid with given dimensions."""
        self.rows = rows
        self.cols = cols
        # Create a 2D list of Cell objects, all dead by default
        self.cells = [
            [Cell() for _ in range(cols)]
            for _ in range(rows)
        ]

    def set_alive(self, row, col):
        """Set a specific cell to alive."""
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.cells[row][col].alive = True

    def count_live_neighbors(self, row, col):
        """Count the number of live neighbors around a cell."""
        count = 0
        # Check all 8 directions around the cell
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue  # Skip the cell itself
                neighbor_row = row + dr
                neighbor_col = col + dc
                # Fixed borders: ignore out-of-bounds neighbors
                if 0 <= neighbor_row < self.rows and 0 <= neighbor_col < self.cols:
                    if self.cells[neighbor_row][neighbor_col].alive:
                        count += 1
        return count

    def count_live_cells(self):
        """Return the total number of live cells in the grid."""
        return sum(
            1 for row in self.cells
            for cell in row
            if cell.alive
        )

    def display(self, generation):
        """Display the current state of the grid."""
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"  Generation: {generation} | Live cells: {self.count_live_cells()}")
        print("  +" + "-" * (self.cols * 2) + "+")
        for row in self.cells:
            print("  |" + " ".join(str(cell) for cell in row) + "|")
        print("  +" + "-" * (self.cols * 2) + "+")


# ============================================================
# Classe Game
# ============================================================

class Game:
    """A class to represent Conway's Game of Life."""

    # Bonus: max size set to 10,000 to avoid memory overflow
    MAX_SIZE = 10000

    def __init__(self, rows, cols, max_generations=50, delay=0.2):
        """Initialize the game with grid dimensions and settings."""
        self.rows = min(rows, self.MAX_SIZE)
        self.cols = min(cols, self.MAX_SIZE)
        self.max_generations = max_generations
        self.delay = delay  # Delay between generations in seconds
        self.generation = 0
        self.grid = Grid(self.rows, self.cols)

    def seed_random(self, density=0.3):
        """Seed the grid with random live cells based on density."""
        for row in range(self.rows):
            for col in range(self.cols):
                if random.random() < density:
                    self.grid.set_alive(row, col)

    def seed_pattern(self, pattern, offset_row=0, offset_col=0):
        """
        Seed the grid with a specific pattern.
        Pattern is a list of (row, col) tuples.
        """
        for (r, c) in pattern:
            self.grid.set_alive(r + offset_row, c + offset_col)

    def next_generation(self):
        """
        Compute the next generation using Conway's rules:
        1. Live cell < 2 live neighbors  -> dies (underpopulation)
        2. Live cell with 2 or 3 neighbors -> survives
        3. Live cell > 3 live neighbors  -> dies (overpopulation)
        4. Dead cell with exactly 3 neighbors -> becomes alive (reproduction)
        """
        new_grid = Grid(self.rows, self.cols)
        for row in range(self.rows):
            for col in range(self.cols):
                live_neighbors = self.grid.count_live_neighbors(row, col)
                is_alive = self.grid.cells[row][col].alive

                if is_alive:
                    # Rules 1, 2, 3
                    if live_neighbors in (2, 3):
                        new_grid.set_alive(row, col)
                    # Otherwise the cell dies (rules 1 & 3)
                else:
                    # Rule 4
                    if live_neighbors == 3:
                        new_grid.set_alive(row, col)

        self.grid = new_grid
        self.generation += 1

    def is_stable(self, previous_count):
        """Check if the grid has no live cells or is stable."""
        current_count = self.grid.count_live_cells()
        return current_count == 0 or current_count == previous_count

    def run(self):
        """Run the game for max_generations or until stable."""
        previous_count = -1

        for _ in range(self.max_generations):
            self.grid.display(self.generation)
            time.sleep(self.delay)

            # Stop if no live cells or grid is stable
            if self.is_stable(previous_count):
                print("\n  Game over: grid is stable or all cells are dead.")
                break

            previous_count = self.grid.count_live_cells()
            self.next_generation()

        else:
            print(f"\n  Reached max generations ({self.max_generations}).")


# ============================================================
# Patterns célèbres
# ============================================================

# Blinker (oscillateur période 2)
BLINKER = [(0, 0), (0, 1), (0, 2)]

# Glider (se déplace en diagonale)
GLIDER = [
    (0, 1),
    (1, 2),
    (2, 0), (2, 1), (2, 2)
]

# Block (stable)
BLOCK = [
    (0, 0), (0, 1),
    (1, 0), (1, 1)
]

# Toad (oscillateur période 2)
TOAD = [
    (0, 1), (0, 2), (0, 3),
    (1, 0), (1, 1), (1, 2)
]

# Beacon (oscillateur période 2)
BEACON = [
    (0, 0), (0, 1),
    (1, 0),
    (2, 3),
    (3, 2), (3, 3)
]


# ============================================================
# Main
# ============================================================

def main():
    """Main function to run different Game of Life scenarios."""

    print("Conway's Game of Life\n")
    print("Choose a starting pattern:")
    print("1. Random")
    print("2. Glider")
    print("3. Blinker")
    print("4. Block (stable)")
    print("5. Toad")
    print("6. Beacon")

    choice = input("\nEnter choice (1-6): ").strip()

    # Game settings
    rows, cols = 20, 40
    game = Game(rows=rows, cols=cols, max_generations=100, delay=0.15)

    if choice == "1":
        game.seed_random(density=0.3)

    elif choice == "2":
        # Place glider near top-left
        game.seed_pattern(GLIDER, offset_row=2, offset_col=2)

    elif choice == "3":
        # Place blinker in center
        game.seed_pattern(BLINKER, offset_row=rows // 2, offset_col=cols // 2)

    elif choice == "4":
        # Place block in center
        game.seed_pattern(BLOCK, offset_row=rows // 2, offset_col=cols // 2)

    elif choice == "5":
        # Place toad in center
        game.seed_pattern(TOAD, offset_row=rows // 2, offset_col=cols // 2)

    elif choice == "6":
        # Place beacon in center
        game.seed_pattern(BEACON, offset_row=rows // 2, offset_col=cols // 2)

    else:
        print("Invalid choice. Using random pattern.")
        game.seed_random(density=0.3)

    game.run()


if __name__ == "__main__":
    main()