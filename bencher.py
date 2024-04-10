from algs.DFS import DFS
from algs.BFS import BFS
from graph import Graph, Node


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
    print("BFS Traversal:", bfs_traversal.traverse("A", "C"))

    # Using DFS traversal
    dfs_traversal = DFS(graph)
    print("DFS Traversal:", dfs_traversal.traverse("A", "C"))