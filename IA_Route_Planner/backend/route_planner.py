import heapq
from collections import deque
from utils import heuristic  # Import heuristic from utils

def dijkstra(adjacency, start, goal, closed_set):
    """
    Dijkstra's algorithm for shortest path.
    Complexity: O((V+E) log V) with binary heap.
    Returns: (path, cost, expanded_nodes)
    """
    if start not in adjacency or goal not in adjacency:
        return None, float('inf'), []

    dist = {node: float('inf') for node in adjacency}
    dist[start] = 0
    prev = {node: None for node in adjacency}
    pq = [(0, start)]  # (distance, node)
    expanded = []

    while pq:
        current_dist, current = heapq.heappop(pq)
        if current in expanded:
            continue
        expanded.append(current)
        if current == goal:
            break
        if current in closed_set:
            continue  # Skip closed nodes
        for neighbor, cost in adjacency[current]:
            if neighbor in closed_set:
                continue
            new_dist = current_dist + cost
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                prev[neighbor] = current
                heapq.heappush(pq, (new_dist, neighbor))

    if dist[goal] == float('inf'):
        return None, float('inf'), expanded

    # Reconstruct path
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = prev[current]
    path.reverse()
    return path, dist[goal], expanded

def astar(adjacency, start, goal, closed_set, h_func=None):
    """
    A* algorithm for shortest path.
    If h_func is None, uses default heuristic (0).
    Complexity: O((V+E) log V) with admissible heuristic.
    Returns: (path, cost, expanded_nodes)
    """
    if h_func is None:
        h_func = lambda n: 0  # Default heuristic

    if start not in adjacency or goal not in adjacency:
        return None, float('inf'), []

    dist = {node: float('inf') for node in adjacency}
    dist[start] = 0
    prev = {node: None for node in adjacency}
    pq = [(h_func(start), start)]  # (f_score, node)
    expanded = []

    while pq:
        _, current = heapq.heappop(pq)
        if current in expanded:
            continue
        expanded.append(current)
        if current == goal:
            break
        if current in closed_set:
            continue
        for neighbor, cost in adjacency[current]:
            if neighbor in closed_set:
                continue
            new_dist = dist[current] + cost
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                prev[neighbor] = current
                f_score = new_dist + h_func(neighbor)
                heapq.heappush(pq, (f_score, neighbor))

    if dist[goal] == float('inf'):
        return None, float('inf'), expanded

    # Reconstruct path
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = prev[current]
    path.reverse()
    return path, dist[goal], expanded

def bfs(adjacency, start, goal, closed_set):
    """
    BFS for shortest path (unweighted).
    Complexity: O(V+E)
    Returns: (path, cost, expanded_nodes)
    Note: Cost is number of edges, not actual cost.
    """
    if start not in adjacency or goal not in adjacency:
        return None, float('inf'), []

    queue = deque([start])
    prev = {node: None for node in adjacency}
    dist = {node: float('inf') for node in adjacency}
    dist[start] = 0
    expanded = []

    while queue:
        current = queue.popleft()
        if current in expanded:
            continue
        expanded.append(current)
        if current == goal:
            break
        if current in closed_set:
            continue
        for neighbor, _ in adjacency[current]:  # Ignore cost for BFS
            if neighbor in closed_set or dist[neighbor] != float('inf'):
                continue
            dist[neighbor] = dist[current] + 1  # Edge count
            prev[neighbor] = current
            queue.append(neighbor)

    if dist[goal] == float('inf'):
        return None, float('inf'), expanded

    # Reconstruct path
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = prev[current]
    path.reverse()
    return path, dist[goal], expanded  # Cost is edge count