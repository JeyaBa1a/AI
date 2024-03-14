def constraint_satisfied(map, country, color, assignment):
    for neighbor in map[country]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtracking_search(map, assignment={}):
    if len(assignment) == len(map):
        return assignment
    unassigned = [country for country in map if country not in assignment]
    first = unassigned[0]
    for color in colors:
        if constraint_satisfied(map, first, color, assignment):
            assignment[first] = color
            result = backtracking_search(map, assignment)
            if result is not None:
                return result
            assignment.pop(first, None)
    return None

if __name__ == "__main__":
    map = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'SA', 'Q'],
        'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
        'Q': ['NT', 'SA', 'NSW'],
        'NSW': ['SA', 'Q', 'V'],
        'V': ['SA', 'NSW', 'T'],
        'T': ['V']
    }
    colors = ['red', 'green', 'blue']
    assignment = backtracking_search(map)
    if assignment is None:
        print("No solution found!")
    else:
        print(assignment)
