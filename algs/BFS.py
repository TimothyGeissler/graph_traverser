from algs.SuperTraverser import SuperTraverser


class BFS(SuperTraverser):
    def __init__(self, graph):
        super().__init__(graph)

    def traverse(self, start_node_name, end_node_name):
        if start_node_name not in self.graph.nodes:
            return None

        visited = set()
        queue = [start_node_name]
        traversal_result = []

        while queue:
            current_node_name = queue.pop(0)
            if current_node_name == end_node_name:
                return traversal_result
            if current_node_name not in visited:
                traversal_result.append(current_node_name)
                visited.add(current_node_name)
                current_node = self.graph.nodes[current_node_name]
                for neighbor in current_node.neighbors:
                    if neighbor.name not in visited:
                        queue.append(neighbor.name)

        return traversal_result
