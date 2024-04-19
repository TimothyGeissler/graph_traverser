from algs.SuperTraverser import SuperTraverser


class DFS(SuperTraverser):
    def __init__(self, graph):
        super().__init__(graph)

    def traverse(self, start_node_name, end_node_name):
        if start_node_name not in self.graph.nodes:
            return None

        visited = set()
        path = []

        def dfs_util(node_name):
            #print("\tVisiting: " + node_name)
            visited.add(node_name)
            path.append(node_name)
            if node_name == end_node_name:  # Found end of path
                #print("\tReached dest: " + node_name + "=" + end_node_name)
                return True  # Signal that destination node is found
            #print("\tChecking neighbours=" + str(self.graph.nodes[node_name].neighbors))
            for neighbor in self.graph.nodes[node_name].neighbors:
                if neighbor.name not in visited:
                    #print("\tUnvisited neighbour=" + neighbor.name)
                    if dfs_util(neighbor.name):  # Recursively check the neighbor
                        return True  # If destination node found, return True
            path.pop()  # Backtrack if destination node not found from this node
            return False  # Signal that destination node is not found

        dfs_util(start_node_name)
        return len(path), path, visited  # Return the path and visited nodes
