import heapq
import math
import sys

from algs.SuperTraverser import SuperTraverser


class AStar(SuperTraverser):
        def __init__(self, graph):
            super().__init__(graph)

        def heuristic(self, nodeA, nodeB):
            xA, yA = self.graph.nodes[nodeA].x, self.graph.nodes[nodeA].y
            xB, yB = self.graph.nodes[nodeB].x, self.graph.nodes[nodeB].y
            return math.sqrt((xB-xA)**2 + (yB-yA)**2)

        def traverse(self, start_node_name, end_node_name):
            # Priority Queue for Nodes to Explore
            unexplored_nodes = []

            # Set to store nodes we've explored
            explored_nodes = set()
            #Initialize shortest distances and previous node dictionaries
            shortest_dist = {node: sys.maxsize for node in self.graph.get_nodes()}
            shortest_dist[start_node_name] = 0

            previous_nodes = {node: None for node in self.graph.get_nodes()}
            #Push the start node into the unexplored nodes with its distance from the heuristic
            heapq.heappush(unexplored_nodes, (
                self.heuristic(start_node_name, end_node_name), start_node_name, 0))

            while unexplored_nodes:
                # Pop node with lowest estimated total cost
                estimated_total_cost, current_node, current_distance = \
                    heapq.heappop(unexplored_nodes)
                # Add current node to set of explored nodes
                explored_nodes.add(current_node)

                # If we reach the end node, we stop the search
                if current_node == end_node_name:
                    break
                # Get current node's object to explore its neighbors
                current_node_obj = self.graph.nodes[current_node]

                # Go through all the neighbors
                for neighbor_node in current_node_obj.neighbors:
                    neighbor = neighbor_node.name

                    # If we've already looked at this node, then skip
                    if neighbor in explored_nodes:
                        continue

                    edge_weight = 1
                    potential_distance = current_distance + edge_weight

                    # If we found a shorter path to the neighbor
                    if potential_distance < shortest_dist[neighbor]:
                        # Update the distance and previous node
                        shortest_dist[neighbor] = potential_distance
                        previous_nodes[neighbor] = current_node

                        # Calculate the estimated total cost (f value)
                        estimated_total_cost = potential_distance + \
                                               self.heuristic(neighbor,
                                                              end_node_name)
                        # Push the neighbor node with the estimated total cost into the heap
                        heapq.heappush(unexplored_nodes, (
                        estimated_total_cost, neighbor, potential_distance))

            # Reconstruct the path from the end node to the start node
            path = []
            current = end_node_name
            while current is not None:
                path.insert(0, current)
                current = previous_nodes[current]

            # Return the shortest distance and the path as a tuple
            return shortest_dist[end_node_name], path, explored_nodes
