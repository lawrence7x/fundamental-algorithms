# Breath First Search
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        if node not in visited:
            visited.add(node)
            queue.extend(graph[node])  # Add neighbors to the queue
    
    return result

# Graph definition
graph = {
    'L': ['A', 'W'],
    'A': ['R', 'E'],
    'W': ['N'],
    'R': [],
    'N': ['C', 'E'],
    'C': [],
    'E': []
}

# Perform BFS
output = bfs(graph, 'L')
print(" ".join(output))
