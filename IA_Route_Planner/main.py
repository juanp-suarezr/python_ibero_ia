#!/usr/bin/env python3
import argparse
import time
import os
import sys

# Add backend to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

from logic_parser import KnowledgeBaseParser
from route_planner import dijkstra, astar, bfs

def main():
    parser = argparse.ArgumentParser(description='Route Planner CLI')
    parser.add_argument('--kb', default='backend/knowledge_base.txt', help='Path to knowledge base file')
    parser.add_argument('--start', required=True, help='Start station')
    parser.add_argument('--goal', required=True, help='Goal station')
    parser.add_argument('--algorithm', choices=['dijkstra', 'astar', 'bfs'], default='dijkstra', help='Algorithm to use')
    parser.add_argument('--closed', nargs='*', default=[], help='Additional closed stations')

    args = parser.parse_args()

    # Parse KB
    kb_parser = KnowledgeBaseParser(args.kb)
    if not kb_parser.parse():
        print("Errors in knowledge base:")
        for error in kb_parser.get_errors():
            print(error)
        return

    adjacency = kb_parser.get_adjacency()
    kb_closed = kb_parser.get_closed()
    total_closed = kb_closed.union(set(args.closed))

    # Validate start and goal
    if args.start not in adjacency or args.goal not in adjacency:
        print("Error: Start or goal not in knowledge base")
        return

    # Run algorithm
    start_time = time.time()
    if args.algorithm == 'dijkstra':
        path, cost, expanded = dijkstra(adjacency, args.start, args.goal, total_closed)
    elif args.algorithm == 'astar':
        path, cost, expanded = astar(adjacency, args.start, args.goal, total_closed)
    elif args.algorithm == 'bfs':
        path, cost, expanded = bfs(adjacency, args.start, args.goal, total_closed)

    end_time = time.time()
    elapsed_ms = (end_time - start_time) * 1000

    if path is None:
        print("No path found")
        return

    print(f"Path: {path}")
    print(f"Cost: {cost}")
    print(f"Expanded nodes: {expanded}")
    print(f"Time: {elapsed_ms:.2f} ms")

if __name__ == '__main__':
    main()