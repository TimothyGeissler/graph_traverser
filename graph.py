class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        if isinstance(node, Node) and node.name not in self.nodes:
            self.nodes[node.name] = node
            return True
        else:
            return False

    def add_edge(self, node1_name, node2_name):
        if node1_name in self.nodes and node2_name in self.nodes:
            node1 = self.nodes[node1_name]
            node2 = self.nodes[node2_name]
            node1.add_neighbor(node2)
            return True
        else:
            return False

    def traverse_bfs(self, start_node_name):
        if start_node_name not in self.nodes:
            return None

        visited = set()
        queue = [start_node_name]
        traversal_result = []

        while queue:
            current_node_name = queue.pop(0)
            if current_node_name not in visited:
                traversal_result.append(current_node_name)
                visited.add(current_node_name)
                current_node = self.nodes[current_node_name]
                for neighbor in current_node.neighbors:
                    if neighbor.name not in visited:
                        queue.append(neighbor.name)

        return traversal_result

    def traverse_dfs(self, start_node_name):
        if start_node_name not in self.nodes:
            return None

        visited = set()
        traversal_result = []

        def dfs_util(node_name):
            visited.add(node_name)
            traversal_result.append(node_name)
            for neighbor in self.nodes[node_name].neighbors:
                if neighbor.name not in visited:
                    dfs_util(neighbor.name)

        dfs_util(start_node_name)
        return traversal_result

    def get_nodes(self):
        return list(self.nodes)

class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def add_neighbor(self, neighbor):
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)