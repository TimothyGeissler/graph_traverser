class Graph:
    def __init__(self, adjacency_matrix=None, coordinates=None):
        self.nodes = {}
        if adjacency_matrix is not None:
            self.construct_graph_from_matrix(adjacency_matrix)
        if coordinates is not None:
            self.set_coordinates(coordinates)

    def construct_graph_from_matrix(self, adjacency_matrix):
        num_nodes = len(adjacency_matrix)
        # print("constructing from " + str(num_nodes) + "x" + str(num_nodes) + " matrix")
        for i in range(num_nodes):
            node_name = f"Node_{i}"
            self.nodes[node_name] = Node(node_name)

        for i in range(num_nodes):
            for j in range(num_nodes):
                if adjacency_matrix[i][j] == 1:
                    node1_name = f"Node_{i}"
                    node2_name = f"Node_{j}"
                    # print("Added edge from " + str(i) + "->" + str(j))
                    self.add_edge(node1_name, node2_name)

    # Add coords to graph
    def set_coordinates(self, coordinates):
        if len(coordinates) != len(self.nodes):
            raise ValueError("Number of coordinates does not match the number of nodes")
        for i, (x, y) in enumerate(coordinates):
            node_name = f"Node_{i}"
            if node_name in self.nodes:
                self.nodes[node_name].x = x
                self.nodes[node_name].y = y

    def add_node(self, node, x=None, y=None):
        if isinstance(node, Node) and node.name not in self.nodes:
            node.x = x
            node.y = y
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
    def __init__(self, name, x=None, y=None):
        self.name = name
        self.neighbors = []
        self.x = x
        self.y = y

    def add_neighbor(self, neighbor):
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)
