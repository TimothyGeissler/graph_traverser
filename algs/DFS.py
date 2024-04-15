from algs.SuperTraverser import SuperTraverser


class DFS(SuperTraverser):
    def __init__(self, graph):
        super().__init__(graph)

    def traverse(self, start_node_name, end_node_name):
        if start_node_name not in self.graph.nodes:
            return None

        visited = set()
        traversal_result = []

        def dfs_util(node_name):
            visited.add(node_name)
            traversal_result.append(node_name)
            if node_name == end_node_name:
                return traversal_result
            for neighbor in self.graph.nodes[node_name].neighbors:
                if neighbor.name not in visited:
                    dfs_util(neighbor.name)

        dfs_util(start_node_name)
        return traversal_result
