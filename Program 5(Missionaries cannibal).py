from collections import deque
def is_valid(state):
    missionaries_left, cannibals_left, boat = state
    missionaries_right = 3 - missionaries_left
    cannibals_right = 3 - cannibals_left

    if missionaries_left > 0 and missionaries_left < cannibals_left:
        return False
    if missionaries_right > 0 and missionaries_right < cannibals_right:
        return False
    return True

def generate_moves(state):
    moves = []
    missionaries_left, cannibals_left, boat = state
    for m in range(3):
        for c in range(3):
            if 1 <= m + c <= 2:
                new_state = (missionaries_left - m, cannibals_left - c, not boat)
                if is_valid(new_state):
                    moves.append((new_state, (m, c)))
    for m in range(3):
        for c in range(3):
            if 1 <= m + c <= 2:
                new_state = (missionaries_left + m, cannibals_left + c, not boat)
                if is_valid(new_state):
                    moves.append((new_state, (-m, -c)))
    return moves

def solve_missionaries_cannibals():
    start_state = (3, 3, True)  
    goal_state = (0, 0, False)  
    visited_states = set()
    queue = deque([(start_state, [])])
    while queue:
        current_state, path = queue.popleft()
        if current_state == goal_state:
            return path
        if current_state not in visited_states:
            visited_states.add(current_state)
            for next_state, move in generate_moves(current_state):
                if next_state not in visited_states:
                    queue.append((next_state, path + [move]))
    return None

def print_solution(path):
    if path:
        print("Solution found:")
        for i, move in enumerate(path):
            missionaries, cannibals = abs(move[0]), abs(move[1])
            if move[0] < 0 or move[1] < 0:
                print(f"{i + 1}. Move {missionaries} missionaries and {cannibals} cannibals from right to left.")
            else:
                print(f"{i + 1}. Move {missionaries} missionaries and {cannibals} cannibals from left to right.")
    else:
        print("No solution found.")

solution_path = solve_missionaries_cannibals()
print_solution(solution_path)
