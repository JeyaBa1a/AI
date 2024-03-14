def water_jug_problem(max_a, max_b, target):
    path = []
    visited_states = set()
    def dfs(a, b):
        if a == target or b == target:
            return True
        if (a, b) in visited_states:
            return False
        visited_states.add((a, b))
        # Fill jug A
        if a < max_a:
            path.append(f"Fill jug A ({a}/{max_a})")
            if dfs(max_a, b):
                return True
            path.pop()
        # Fill jug B
        if b < max_b:
            path.append(f"Fill jug B ({b}/{max_b})")
            if dfs(a, max_b):
                return True
            path.pop()
        # Empty jug A
        if a > 0:
            path.append(f"Empty jug A ({a}/{max_a})")
            if dfs(0, b):
                return True
            path.pop()
        # Empty jug B
        if b > 0:
            path.append(f"Empty jug B ({b}/{max_b})")
            if dfs(a, 0):
                return True
            path.pop()
        # Pour water from A to B
        if a > 0 and b < max_b:
            amount = min(a, max_b - b)
            path.append(f"Pour {amount} gallons from A to B ({a}/{max_a}, {b}/{max_b})")
            if dfs(a - amount, b + amount):
                return True
            path.pop()
        # Pour water from B to A
        if b > 0 and a < max_a:
            amount = min(b, max_a - a)
            path.append(f"Pour {amount} gallons from B to A ({a}/{max_a}, {b}/{max_b})")
            if dfs(a + amount, b - amount):
                return True
            path.pop()
        return False
    if dfs(0, 0):
        return path
    else:
        return "No solution found."
max_a = 4
max_b = 3
target = 2
solution = water_jug_problem(max_a, max_b, target)
print("\n".join(solution))
