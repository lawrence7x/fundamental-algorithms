import heapq
import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph(graph):
    G = nx.DiGraph()  # Create a directed graph
    for node, neighbors in graph.items():
        for neighbor, weight in neighbors:
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G)  # Layout for visualization
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold')
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title("Graph Visualization")
    plt.show()

def dijkstra(graph, start):
    priority_queue = [(0, start)]  # (distance, node)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    visited = set()

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue
        visited.add(current_node)

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example graph as an adjacency list
graph = {
    'L': [('A', 1), ('W', 4)],
    'A': [('R', 1)],
    'W': [('E', 4)],
    'R': [('N', 6)],
    'E': [('C', 2)],
    'N': [('E SXP', 4)],
    'C': [('E SXP', 1)]
}

# Visualize the graph
visualize_graph(graph)

# Run Dijkstra's algorithm
start_node = 'A'
shortest_distances = dijkstra(graph, start_node)

# Print the shortest distances from the start node
print(f"Shortest distances from node {start_node}:")
for node, distance in shortest_distances.items():
    print(f"{node}: {distance}")
