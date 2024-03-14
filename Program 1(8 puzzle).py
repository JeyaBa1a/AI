from collections import deque

def find_blank(puzzle):
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == 0:
                return i, j

def is_valid_move(x, y):
    return 0 <= x < 3 and 0 <= y < 3

def generate_moves(puzzle):
    blank_i, blank_j = find_blank(puzzle)
    moves = []

    for dx, dy, move in [(0, -1, 'Left'), (0, 1, 'Right'), (-1, 0, 'Up'), (1, 0, 'Down')]:
        new_i, new_j = blank_i + dx, blank_j + dy
        if is_valid_move(new_i, new_j):
            new_puzzle = [row[:] for row in puzzle]
            new_puzzle[blank_i][blank_j], new_puzzle[new_i][new_j] = new_puzzle[new_i][new_j], new_puzzle[blank_i][blank_j]
            moves.append((new_puzzle, move))

    return moves

def is_solved(puzzle):
    return puzzle == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

def solve_puzzle(initial_puzzle):
    queue = deque([(initial_puzzle, [])])

    while queue:
        current_puzzle, current_path = queue.popleft()

        if is_solved(current_puzzle):
            return current_path

        for next_puzzle, move in generate_moves(current_puzzle):
            queue.append((next_puzzle, current_path + [move]))

    return None

initial_puzzle = [[1, 2, 3],
                  [4, 0, 5],
                  [6, 7, 8]]

solution = solve_puzzle(initial_puzzle)
if solution:
    print("Solution found in", len(solution), "moves:", solution)
else:
    print("No solution found.")
