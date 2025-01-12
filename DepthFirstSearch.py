def dfs(graph, start):
    visited = set()
    result = []

    def dfs_helper(node):
        result.append(node)  # Always add the node to the result
        visited.add(node)    # Mark the node as visited
        for neighbor in graph[node]:
            dfs_helper(neighbor)  # Always visit neighbors

    dfs_helper(start)
    return result

graph = {
    'L': ['A', 'R', 'N'],
    'A': ['W'],
    'R': ['E'],
    'N': ['C'],
    'W': [],
    'E': [],
    'C': ['E']
}

test = dfs(graph, 'L')
print(test)
