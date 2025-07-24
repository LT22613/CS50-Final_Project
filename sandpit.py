def create_grid(rows, cols):
        grid = [[None for _ in range(cols)] for _ in range(rows)]

def print_grid(grid):
        for row in grid:
                print(" | ".join(type(cell).__name__[0] if cell else " " for cell in row))

grid = create_grid(2,2)
print_grid(grid)