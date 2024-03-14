import itertools
def calculate_total_distance(tour, distances):
    total_distance = 0
    n = len(tour)
    for i in range(n):
        total_distance += distances[tour[i % n]][tour[(i + 1) % n]]
    return total_distance
def tsp_brute_force(distances):
    n = len(distances)
    min_distance = float('inf')
    min_tour = None
    for tour in itertools.permutations(range(n)):
        distance = calculate_total_distance(tour, distances)
        if distance < min_distance:
            min_distance = distance
            min_tour = tour
    return min_tour, min_distance
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
min_tour, min_distance = tsp_brute_force(distances)
print("Minimum tour:", min_tour)
print("Minimum distance:", min_distance)
