from flask import Flask, request, jsonify
from flask_cors import CORS
from logic_parser import KnowledgeBaseParser
from route_planner import dijkstra, astar, bfs
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for development

# Load knowledge base
kb_path = os.path.join(os.path.dirname(__file__), 'knowledge_base.txt')
parser = KnowledgeBaseParser(kb_path)
if not parser.parse():
    print("Errors in knowledge base:")
    for error in parser.get_errors():
        print(error)
    exit(1)

adjacency = parser.get_adjacency()
kb_closed = parser.get_closed()

@app.route('/api/route', methods=['POST'])
def route():
    data = request.get_json()
    if not data:
        return jsonify({"status": "error", "message": "No JSON data provided"}), 400

    start = data.get('start')
    goal = data.get('goal')
    algorithm = data.get('algorithm', 'dijkstra')
    closed = data.get('closed', [])

    # Validation
    if not start or not goal:
        return jsonify({"status": "error", "message": "Start and goal are required"}), 400
    if start not in adjacency or goal not in adjacency:
        return jsonify({"status": "error", "message": "Start or goal not in knowledge base"}), 400
    if algorithm not in ['dijkstra', 'astar', 'bfs']:
        return jsonify({"status": "error", "message": "Algorithm must be dijkstra, astar, or bfs"}), 400
    if not isinstance(closed, list):
        return jsonify({"status": "error", "message": "Closed must be a list"}), 400

    # Combine closed sets
    total_closed = kb_closed.union(set(closed))

    # Call algorithm
    if algorithm == 'dijkstra':
        path, cost, expanded = dijkstra(adjacency, start, goal, total_closed)
    elif algorithm == 'astar':
        path, cost, expanded = astar(adjacency, start, goal, total_closed)
    elif algorithm == 'bfs':
        path, cost, expanded = bfs(adjacency, start, goal, total_closed)

    if path is None:
        return jsonify({"status": "error", "message": "No path found"}), 404

    return jsonify({
        "path": path,
        "cost": cost,
        "expanded": expanded,
        "status": "ok"
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)