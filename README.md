# Graph Project README

Implementations of various Graph Traversal algorithms with the aim of benchmarking and comparing implementations across several relevant criteria and performance metrics.

## Contents:

* _bencher.py:_ Benchmarking tools for each graph traversal algorithm. Prints standardized outputs and graphs for relevant metrics. Ensures consistency in testing between each implementation
* _graph.py:_ Basic directed graph object consisting of Nodes. Each Node has an array of other adjacent Node objects, serving as the edge-list.
* _*algs:*_ Implementations of each of the traversal algorithms
* _plots_: Some useful/relevant benchmark results

## Algs
Each of the implementations should inherit from the same superclass (```SuperTraverser.py```) and implement at least the ```traverse()``` method. Note: ```traverse()``` should return an integer value of the number of nodes visted before the target node is reached.

* ```DFS()``` performs a depth-first search on the given graph until the destination node is reached, and returns the path used to reach the destination.
* ```Dijkstra()``` uses Dijkstra's Algorithm to return the shortest path between given nodes, as well as the path length
## Benches
The bencher class relies on inheritance to run the same benchset on all implementations. Uses matplotlib to render graphs of relevant data

* ```performance_plot('DFS')``` runs a scalability benchmark on a given algorithm implementation and returns a runtime vs. graph size plot

TODO:
- Cartesian Nodes (A*)
- Implement more tests/plots
  - efficiency



- A*