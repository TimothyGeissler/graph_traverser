from algs.SuperTraverser import SuperTraverser
import sys
import heapq


class Dijkstra(SuperTraverser):
    def __init__(self, graph):
        super().__init__(graph)

    def traverse(self, start_node_name, end_node_name):
        nodes_dist = []
        # Setting the distances dictionary with default infinity value for all notes
        distances = {node: sys.maxsize for node in self.graph.get_nodes()}
        # Set distances for start node to - and push it into the nodes_dist category we created
        distances[start_node_name] = 0
        previous = {node: None for node in self.graph.get_nodes()}
        heapq.heappush(nodes_dist, (0, start_node_name))

        while nodes_dist:
            current_distance, current_node = heapq.heappop(nodes_dist)

            # if end node, stop processing
            if current_node == end_node_name:
                break

            # Let's look at all neighbors of the current node
            current_node_obj = self.graph.nodes[current_node]

            for neighbor_node in current_node_obj.neighbors:
                neighbor = neighbor_node.name

                # Find tentative distance to neighbor
                edge_weight = 1
                potential_distance = current_distance + edge_weight

                # If shorter path is found, update distance
                if potential_distance < distances[neighbor]:
                    distances[neighbor] = potential_distance
                    previous[neighbor] = current_node
                    heapq.heappush(nodes_dist, (potential_distance, neighbor))
        # Rewrites the path from end node to start node
        path = []
        current = end_node_name
        while current is not None:
            path.insert(0, current)
            current = previous[current]

        # Return the shortest distance and the path as a tuple
        return distances[end_node_name], path
