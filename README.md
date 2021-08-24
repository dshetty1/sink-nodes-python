# sink-nodes-python
### Description:
This program identifies the nodes in each sink component in an SCC graph that is generated from a standard graph.
 - First, build the initial graph from the input
 - Next, run Kosaraju's algorithm on the standard graph in order to obtain the SCC graph
 - Identify the nodes in each sink

Assume all edges are one-way.

A sink component of an SCC graph is defined as a compononent without outgoing edges. Therefore, all the nodes within sink components can be considered safe nodes, as moving to 

### Input:


ex. <br>
6 7
0 2
1 3
2 4
3 5
4 0
5 0
5 1

### Output:


ex.
0 2 4 

