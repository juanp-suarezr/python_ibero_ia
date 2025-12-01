import re
from collections import defaultdict

class KnowledgeBaseParser:
    def __init__(self, kb_file_path):
        self.kb_file_path = kb_file_path
        self.adjacency = defaultdict(list)
        self.closed = set()
        self.nodes = set()
        self.errors = []

    def parse(self):
        """Parse the knowledge base file and populate adjacency, closed, and nodes."""
        try:
            with open(self.kb_file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except FileNotFoundError:
            self.errors.append(f"Error: Knowledge base file '{self.kb_file_path}' not found.")
            return False

        for line_num, line in enumerate(lines, start=1):
            line = line.strip()
            if not line or line.startswith('%'):
                continue
            if not self._parse_line(line, line_num):
                return False
        return len(self.errors) == 0

    def _parse_line(self, line, line_num):
        """Parse a single line for edge or closed facts."""
        # Match edge(StationA, StationB, Cost).
        edge_pattern = r'^edge\((\w+),\s*(\w+),\s*(\d+(?:\.\d+)?)\)\.$'
        closed_pattern = r'^closed\((\w+)\)\.$'

        if re.match(edge_pattern, line):
            match = re.search(edge_pattern, line)
            node1, node2, cost_str = match.groups()
            try:
                cost = float(cost_str)
            except ValueError:
                self.errors.append(f"Line {line_num}: Invalid cost '{cost_str}', must be a number.")
                return False
            self.adjacency[node1].append((node2, cost))
            self.nodes.add(node1)
            self.nodes.add(node2)
        elif re.match(closed_pattern, line):
            match = re.search(closed_pattern, line)
            node = match.group(1)
            self.closed.add(node)
            self.nodes.add(node)
        else:
            self.errors.append(f"Line {line_num}: Invalid syntax '{line}'. Expected edge(Node,Node,Cost). or closed(Node).")
            return False
        return True

    def get_adjacency(self):
        return dict(self.adjacency)

    def get_closed(self):
        return self.closed.copy()

    def get_nodes(self):
        return self.nodes.copy()

    def get_errors(self):
        return self.errors.copy()