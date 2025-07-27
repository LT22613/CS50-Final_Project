import random
from game_model import *

class Maze:
    """Defines a Maze object modelling a maze for the hero to traverse.
    
    A maze is represented as a 2D grid where each cell can contain game objects
    (like monsters, items, or the hero). The maze tracks the hero's position
    and provides methods to manipulate objects within the grid.
    
    Attributes:
        rows (int): Number of rows in the maze grid
        cols (int): Number of columns in the maze grid
        grid (List[List[Optional[Object]]]): 2D list representing maze cells
        hero_position (Tuple[int, int]): Current (row, col) position of hero
    """
    def __init__(self, rows=5, cols=5):
        """Initializes an empty maze of specified dimensions.

        Args:
            rows (int): Number of rows in the maze. Defaults to 5.
            cols (int): Number of columns in the maze. Defaults to 5.
        """
        self.rows = rows
        self.cols = cols
        # Create empty 2D grid filled with None values
        self.grid = [[None, Monster("Goblin"), None, TreasureChest(), None],
            [HealingPotion(), None, Monster("Orc"), None, None],
            [None, TreasureChest(), None, Monster("Troll"), None],
            [Monster("Skeleton"), None, HealingPotion(), None, Shopkeeper()],
            [None, None, Monster("Dragon"), TreasureChest(), None]]
        self.hero_position = (0, 0)  # Default starting position at top-left

    def place_object(self, row: int, col: int, obj: object) -> None:
        """Places an object at the specified position in the maze.
        
        Args:
            row (int): Row index for object placement
            col (int): Column index for object placement
            obj (object): Game object to place in the cell
        """
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.grid[row][col] = obj

    def get_object(self, row: int, col: int) -> object:
        """Retrieves the object at the specified position.
        
        Args:
            row (int): Row index to check
            col (int): Column index to check
            
        Returns:
            object: The object at specified position, or None if empty/invalid
        """
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.grid[row][col]
        return None

    def remove_object(self, row: int, col: int) -> None:
        """Removes any object at the specified position.
        
        Args:
            row (int): Row index to clear
            col (int): Column index to clear
        """
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.grid[row][col] = None

    def update_hero_position(self, new_row: int, new_col: int) -> None:
        """Updates the hero's position if the new coordinates are valid.
        
        Args:
            new_row (int): New row position for hero
            new_col (int): New column position for hero
        """
        if 0 <= new_row < self.rows and 0 <= new_col < self.cols:
            self.hero_position = (new_row, new_col)

    def print_maze(self) -> None:
        """Displays the current state of the maze in the console.
        
        Prints a grid where:
        - 'H' represents the hero's position
        - '.' represents empty cells
        - '|' separates columns for readability
        """
        print("\nCurrent Maze View:")
        for r in range(self.rows):
            row_display = []
            for c in range(self.cols):
                if (r, c) == self.hero_position:
                    row_display.append(" H ")  # Hero position
                else:
                    row_display.append(" . ")  # Empty cell
            print(" | ".join(row_display))
        print()  # Extra spacing

if __name__ == "__main__":
    # Example usage
    maze = Maze()  # Create default 5x5 maze

    # Demonstrate hero movement
    maze.update_hero_position(0, 0)  # Move hero to starting position
    maze.print_maze()                # Display initial state

    maze.update_hero_position(4, 4)  # Move hero to new position
    maze.print_maze()                # Display updated state

