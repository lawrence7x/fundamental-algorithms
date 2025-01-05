# Breath First Search
from collections import deque

def bfs(graph, start):
    visited = set()       # To track visited nodes
    queue = deque([start])  # Initialize queue with the start node
    visited.add(start)     # Mark the start node as visited

    while queue:
        node = queue.popleft()  # Dequeue a node
        print(node, end=" ")    # Process the node (here, we print it)

        # Enqueue all unvisited neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example usage:
graph = {
    0: [1, 2],
    1: [3, 4],
    2: [5, 6],
    3: [],
    4: [],
    5: [],
    6: []
}
bfs(graph, 0)  # Output: 0 1 2 3 4 5 6
