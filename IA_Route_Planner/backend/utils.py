# Utils for route planner

# Heuristic function for A*
# Currently returns 0 (admissible), but can be extended for coordinates
def heuristic(node):
    """
    Heuristic for A* algorithm.
    Currently returns 0 for all nodes (reduces to Dijkstra).
    Can be extended to Manhattan or Euclidean if coordinates are provided.
    """
    # Example: if coordinates are available, e.g., coords = {'EstacionA': (0,0), ...}
    # return abs(coords[node][0] - coords[goal][0]) + abs(coords[node][1] - coords[goal][1])
    return 0

# Placeholder for future extensions
def manhattan_distance(node1, node2, coords):
    """Calculate Manhattan distance if coordinates are provided."""
    if node1 in coords and node2 in coords:
        x1, y1 = coords[node1]
        x2, y2 = coords[node2]
        return abs(x1 - x2) + abs(y1 - y2)
    return 0