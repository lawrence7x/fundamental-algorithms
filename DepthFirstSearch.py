def dfs(graph, start):
    visited = set()
    result = []

    def dfs_helper(node):
        result.append(node) 
        visited.add(node)    
        for neighbor in graph[node]:
            dfs_helper(neighbor) 

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
