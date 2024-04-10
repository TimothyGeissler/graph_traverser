from algs.DFS import DFS
from algs.BFS import BFS
from graph import Graph, Node

import matplotlib.pyplot as plt
import networkx as nx

def visualize_graph_traversal(graph, traversal_result):
    G = nx.Graph()
    for node_name, node in graph.nodes.items():
        G.add_node(node_name)
        for neighbor in node.neighbors:
            G.add_edge(node_name, neighbor.name)

    pos = nx.spring_layout(G)
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, edge_color='black', linewidths=1,
            font_size=15, arrows=False)
    nx.draw_networkx_nodes(G, pos, nodelist=traversal_result, node_color='r', node_size=1500)
    plt.title('Graph Traversal Visualization')
    plt.show()

if __name__ == "__main__":
    # Example graph setup
    graph = Graph()
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    graph.add_node(node1)
    graph.add_node(node2)
    graph.add_node(node3)
    graph.add_node(node4)
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("C", "D")

    # Using BFS traversal
    bfs_traversal = BFS(graph)
    bfs_result = bfs_traversal.traverse("A", "C")
    print("BFS Traversal:", bfs_result)
    visualize_graph_traversal(graph, bfs_result)

    # Using DFS traversal
    dfs_traversal = DFS(graph)
    print("DFS Traversal:", dfs_traversal.traverse("A", "C"))