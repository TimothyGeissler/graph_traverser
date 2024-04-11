class SuperTraverser:
    def __init__(self, graph):
        self.graph = graph

    def traverse(self, start_node_name, dest_node_name):
        raise NotImplementedError("Subclasses must implement the traverse method")
        # return path, visited
