import heapq

# Function to calculate the Manhattan distance heuristic
def manhattan_distance(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

# Function to find neighbors of a given position in the grid
def get_neighbors(grid, current):
    neighbors = []
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dx, dy in directions:
        x, y = current[0] + dx, current[1] + dy
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != '#':
            neighbors.append((x, y))
    return neighbors

# Function to implement A* algorithm
def astar(grid, start, goal):
    heap = [(0, start)]
    visited = set()
    costs = {start: 0}
    parents = {start: None}

    while heap:
        current_cost, current = heapq.heappop(heap)

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parents[current]
            return path[::-1]

        visited.add(current)

        for neighbor in get_neighbors(grid, current):
            new_cost = costs[current] + 1
            if neighbor not in costs or new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                priority = new_cost + manhattan_distance(neighbor, goal)
                heapq.heappush(heap, (priority, neighbor))
                parents[neighbor] = current

    return None

# Example usage
grid = [
    ['.', '.', '.', '.', '.'],
    ['.', '#', '#', '#', '.'],
    ['.', '.', '.', '#', '.'],
    ['.', '#', '.', '.', '.'],
    ['.', '.', '.', '.', '.']
]
start = (0, 0)
goal = (4, 4)

path = astar(grid, start, goal)
if path:
    print("Path found:", path)
else:
    print("No path found.")
