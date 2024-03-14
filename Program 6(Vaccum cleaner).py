# Function to move the vacuum cleaner
def move_vacuum_cleaner(grid, pos):
    n = len(grid)
    m = len(grid[0])

    # Check if the current cell is dirty
    if grid[pos[0]][pos[1]] == 'D':
        print(f"Cleaning cell {pos}")

    # Move to the next cell
    if pos[1] < m - 1:  # Move right if possible
        return pos[0], pos[1] + 1
    elif pos[0] < n - 1:  # Move down if possible
        return pos[0] + 1, pos[1]
    elif pos[1] > 0:  # Move left if possible
        return pos[0], pos[1] - 1
    elif pos[0] > 0:  # Move up if possible
        return pos[0] - 1, pos[1]
    else:
        return None  # Nowhere to move

# Function to clean the entire grid
def clean_grid(grid):
    n = len(grid)
    m = len(grid[0])

    # Start from the top-left corner
    pos = (0, 0)

    while pos is not None:
        pos = move_vacuum_cleaner(grid, pos)

# Example usage
grid = [
    ['D', 'C', 'D', 'C'],
    ['C', 'D', 'C', 'D'],
    ['D', 'C', 'D', 'C'],
    ['C', 'D', 'C', 'D']
]

clean_grid(grid)
