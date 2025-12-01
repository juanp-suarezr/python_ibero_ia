import networkx as nx
from utils import heuristic  # Import heuristic from utils

def build_graph(adjacency, closed_set):
    """Build NetworkX graph from adjacency dict, removing closed nodes."""
    G = nx.DiGraph()
    for node, neighbors in adjacency.items():
        if node in closed_set:
            continue
        for neighbor, cost in neighbors:
            if neighbor in closed_set:
                continue
            G.add_edge(node, neighbor, weight=cost)
    return G

def dijkstra(adjacency, start, goal, closed_set):
    """
    Dijkstra's algorithm using NetworkX.
    Returns: (path, cost, expanded_nodes)
    """
    G = build_graph(adjacency, closed_set)
    if start not in G or goal not in G:
        return None, float('inf'), []

    try:
        path = nx.dijkstra_path(G, start, goal, weight='weight')
        cost = nx.dijkstra_path_length(G, start, goal, weight='weight')
        # For expanded nodes, approximate with path (full expansion not directly available)
        expanded = list(G.nodes())  # Simplified
        return path, cost, expanded
    except nx.NetworkXNoPath:
        return None, float('inf'), []

def astar(adjacency, start, goal, closed_set, h_func=None):
    """
    A* algorithm using NetworkX.
    Returns: (path, cost, expanded_nodes)
    """
    if h_func is None:
        h_func = heuristic

    G = build_graph(adjacency, closed_set)
    if start not in G or goal not in G:
        return None, float('inf'), []

    try:
        path = nx.astar_path(G, start, goal, heuristic=h_func, weight='weight')
        cost = nx.astar_path_length(G, start, goal, heuristic=h_func, weight='weight')
        expanded = list(G.nodes())  # Simplified
        return path, cost, expanded
    except nx.NetworkXNoPath:
        return None, float('inf'), []

def bfs(adjacency, start, goal, closed_set):
    """
    BFS using NetworkX (shortest path by edges).
    Returns: (path, cost, expanded_nodes)
    """
    G = build_graph(adjacency, closed_set)
    if start not in G or goal not in G:
        return None, float('inf'), []

    try:
        path = nx.shortest_path(G, start, goal)  # Unweighted
        cost = len(path) - 1  # Number of edges
        expanded = list(G.nodes())  # Simplified
        return path, cost, expanded
    except nx.NetworkXNoPath:
        return None, float('inf'), []