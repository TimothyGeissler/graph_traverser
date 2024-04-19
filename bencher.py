from algs.DFS import DFS
from algs.BFS import BFS
from graph import Graph, Node
from algs.Dijkstra import Dijkstra
from algs.Astar import AStar

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import time
import random


# Visualizes the graph traversal path generated by the algorithm
def visualize_graph(graph, traversal_result=None):
    G = nx.Graph()
    node_count = 0
    for node_name, node in graph.nodes.items():
        G.add_node(node_name)
        node_count += 1
        for neighbor in node.neighbors:
            G.add_edge(node_name, neighbor.name)

    pos = nx.spring_layout(G)
    if all(node.x is not None and node.y is not None for node in graph.nodes.values()):
        # If nodes have coordinates, use them for positioning
        pos = {node_name: (node.x, node.y) for node_name, node in graph.nodes.items()}

    plt.figure(figsize=(8, 6))

    default_node_size = 1500
    max_node_count = 15
    min_node_size = 200
    node_size = max(default_node_size - (node_count - max_node_count) * 50, min_node_size)

    # Determine whether to display node labels based on the number of nodes
    display_node_labels = node_count <= 20

    # Draw the graph with or without node labels
    if display_node_labels:
        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=node_size, edge_color='black', linewidths=1,
                font_size=15, arrows=False)
    else:
        nx.draw(G, pos, with_labels=False, node_color='skyblue', node_size=node_size, edge_color='black', linewidths=1,
                font_size=15, arrows=False)

    if traversal_result:
        path_edges = [(traversal_result[i], traversal_result[i + 1]) for i in range(len(traversal_result) - 1)]
        nx.draw_networkx_nodes(G, pos, nodelist=traversal_result, node_color='r', node_size=node_size)
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)
        plt.title('Graph Traversal Visualization')
    else:
        plt.title('Graph Visualization')

    plt.show()


# Generate adjacency matrix of size n*n
def gen_adj_matrix(n, edge_probability=0.1, seed=None):
    np.random.seed(seed)
    # Initialize an n*n matrix with all zeros
    adjacency_matrix = np.zeros((n, n), dtype=int)

    # Randomly assign 1s to represent directed edges
    for i in range(n):
        for j in range(n):
            # To prevent self-loops, do not allow an edge from a node to itself
            if i != j:
                # Randomly determine whether to assign an edge based on the edge probability
                if np.random.random() < edge_probability:
                    adjacency_matrix[i][j] = 1

    return adjacency_matrix


def gen_cartesian_coords(n, width, height):
    coordinates = []
    for i in range(n):
        x = random.uniform(0, width)
        y = random.uniform(0, height)
        coordinates.append((x, y))
    return coordinates


def measure_average_runtime(alg, n_values, num_iterations, edge_probability, seed=None):
    average_runtimes = []
    for n in n_values:
        runtimes = []
        for _ in range(num_iterations):
            # Generate adjacency matrix for size n with fixed seed
            adjacency_matrix = gen_adj_matrix(n, edge_probability, seed)

            # Create graph object
            adj_graph = Graph(adjacency_matrix)

            # Measure time for DFS traversal from Node_1 to Node_4
            start_time = time.time()

            if alg == 'DFS':
                DFS(adj_graph).traverse("Node_1", "Node_100")
            elif alg == 'BFS':
                BFS(adj_graph).traverse("Node_1", "Node_100")
            elif alg == 'Dijkstra':
                Dijkstra(adj_graph).traverse("Node_1", "Node_99")

            end_time = time.time()

            if alg == 'Astar':
                start_time = time.time()
                coords = gen_cartesian_coords(n, 100, 100)
                coords_graph = Graph(adjacency_matrix, coords)

                AStar(coords_graph).traverse("Node_1", "Node_99")
                end_time = time.time()

            runtimes.append(end_time - start_time)
        average_runtimes.append((n, np.mean(runtimes), np.std(runtimes)))
    return average_runtimes


def measure_average_efficiency(alg, n_values, num_iterations, edge_probability, seed=None):
    average_eff = []
    for n in n_values:
        efficiency = []
        for _ in range(num_iterations):
            # Generate adjacency matrix for size n with fixed seed
            adjacency_matrix = gen_adj_matrix(n, edge_probability, seed)

            # Create graph object
            adj_graph = Graph(adjacency_matrix)

            visited = []
            path = []
            path_len = 0

            if alg == 'DFS':
                path_len, path, visited = DFS(adj_graph).traverse("Node_1", "Node_100")
            elif alg == 'BFS':
                path_len, path, visited = BFS(adj_graph).traverse("Node_1", "Node_100")
            elif alg == 'Dijkstra':
                path_len, path, visited = Dijkstra(adj_graph).traverse("Node_1", "Node_99")
            elif alg == "Astar":
                # Generate coords
                coords = gen_cartesian_coords(n, 100, 100)
                coords_graph = Graph(adjacency_matrix, coords)
                # Run A*
                path_len, path, visited = AStar(coords_graph).traverse("Node_1", "Node_99")

            efficiency.append(len(path) / len(visited))
        average_eff.append((n, np.mean(efficiency), np.std(efficiency)))
    return average_eff


def performance_plot(alg, start=100, end=1001, count=5, iterations=5):
    # Generate n values from 100 to 1000 in increments of 50
    print("Running performance analysis on " + alg)
    increment = (start - end) / count
    n_values = list(range(start, end, 200))

    # Density of graph
    edge_probability = 0.1

    # Number of iterations for averaging runtime

    # Measure average runtime and standard deviation for each n with fixed seed
    average_runtimes = measure_average_runtime(alg, n_values, iterations, edge_probability, seed=42)

    # Extract n, average runtime, and standard deviation values for plotting
    n_values, runtime_values, std_values = zip(*average_runtimes)

    # Plotting
    plt.figure(figsize=(10, 6))
    # plt.errorbar(n_values, runtime_values, yerr=std_values, fmt='o', color='b', ecolor='r', linestyle='-')
    plt.plot(n_values, runtime_values, marker='o', linestyle='-', color='b')
    plt.title('Average Runtime of ' + alg + ' Traversal vs. Graph Size (n) - Graph density=' + str(edge_probability))
    plt.xlabel('Graph Size (n)')
    plt.ylabel('Average Runtime (seconds)')
    plt.grid(True)
    plt.show()


def efficiency_plot(alg, start=100, end=1001, count=5, iterations=5, density=0.1):
    print("Running efficiency analysis on " + alg)
    n_values = list(range(start, end, 200))
    # Density of graph

    average_eff = measure_average_efficiency(alg, n_values, iterations, density, seed=42)

    # Extract n, average runtime, and standard deviation values for plotting
    n_values, eff_values, std_values = zip(*average_eff)

    # Plotting
    plt.figure(figsize=(10, 6))
    # plt.errorbar(n_values, runtime_values, yerr=std_values, fmt='o', color='b', ecolor='r', linestyle='-')
    plt.plot(n_values, eff_values, marker='o', linestyle='-', color='b')
    plt.title('Average Efficiency of ' + alg + ' Traversal vs. Graph Size (n) - Graph density=' + str(density))
    plt.xlabel('Graph Size (n)')
    plt.ylabel('Path Length / # of Visits')
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    # Example graph setup
    graph = Graph()
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")
    node6 = Node("F")
    graph.add_node(node1)
    graph.add_node(node2)
    graph.add_node(node3)
    graph.add_node(node4)
    graph.add_node(node5)
    graph.add_node(node6)
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "C")
    graph.add_edge("B", "D")
    graph.add_edge("B", "F")
    graph.add_edge("C", "E")
    graph.add_edge("D", "E")
    graph.add_edge("E", "F")

    bfs_traversal = BFS(graph)
    bfs_result = bfs_traversal.traverse("A", "C")
    # print("BFS Traversal:", bfs_result)
    # visualize_graph(graph, bfs_result)

    # Using DFS traversal
    dfs_traversal = DFS(graph)
    dfs_result = dfs_traversal.traverse("A", "C")
    # print("DFS Traversal:", dfs_traversal.traverse("A", "C"))
    # visualize_graph(graph, dfs_result)

    # using Dijkstras Traversal - Basic graph
    # dij_traversal = Dijkstra(graph)
    # dijkstra_path = dij_traversal.traverse("A", "F")
    # print("Dijkstra Traversal:", dijkstra_path)
    # visualize_graph(graph, dijkstra_path[1])

    # More complex Dijkstras traversal visualisation
    # cmplx_mat = gen_adj_matrix(50, 0.05, 42)
    # cmplx_graph = Graph(cmplx_mat)
    # d_cmplx = Dijkstra(cmplx_graph)
    # dijkstra_path = d_cmplx.traverse("Node_1", "Node_4")
    # print("Complex path = " + str(dijkstra_path))
    # visualize_graph(cmplx_graph, dijkstra_path[1])

    # More complex A* traversal visualisation
    # cmplx_mat = gen_adj_matrix(50, 0.1, 42)
    # coords = gen_cartesian_coords(50, 100, 100)
    # print("Adj matrix:" + str(cmplx_mat))
    # print("coords: " + str(len(coords)) + " \t" + str(coords))
    #
    # cmplx_graph = Graph(cmplx_mat, coords)
    # print("Graph=" + str(cmplx_graph.nodes))
    # d_cmplx = DFS(cmplx_graph)
    # dijkstra_path = d_cmplx.traverse("Node_1", "Node_38")
    # print("Complex path = " + str(dijkstra_path))
    # visualize_graph(cmplx_graph, dijkstra_path[1])

    # mat = [[0, 1, 1, 0],
    #        [0, 0, 0, 1],
    #        [0, 1, 0, 0],
    #        [0, 0, 0, 0]]
    # adj_graph = Graph(mat)
    # print(adj_graph.nodes)
    # visualize_graph(adj_graph)

    # performance_plot('DFS')
    # performance_plot("Dijkstra")
    # efficiency_plot("DFS", density=0.01)
    efficiency_plot("Astar")
