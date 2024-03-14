from collections import deque
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
def bfs(graph, start):
    visited = set() 
    queue = deque([start])
    while queue:
        node = queue.popleft() 
        if node not in visited:
            print(node)        
            visited.add(node)   
            neighbors = graph.get(node, [])  
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
start_node = 'A'
print("BFS traversal starting from node", start_node)
bfs(graph, start_node)
