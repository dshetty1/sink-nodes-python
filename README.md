# sink-nodes-python
### Description:
This program identifies the nodes in each sink component in an SCC graph, which is generated from a standard graph.

A sink component of an SCC graph is defined as a compononent without outgoing edges. Therefore, all the nodes within sink components can be considered "safe nodes" -- for every node in a sink component that a "safe node" can reach, there is a path from that node back to the "safe node".

In order to identify the sink components and corresponding "safe nodes":
 - First, build the initial graph from the input
 - Next, run Kosaraju's algorithm on the standard graph in order to obtain the SCC graph
 - Identify the nodes in each sink

Assume all edges are one-way.


### Input:
Text file where:

- First line is the total number of nodes and edges
- Each subsequent line identifies the path from one node to another

ex. <br>
6 7 <br>
0 2 <br>
1 3 <br>
2 4 <br>
3 5 <br>
4 0 <br>
5 0 <br>
5 1 <br>

This can also be done in the same format as a standard input on the command line. This code is commented out at the bottom of the file.

### Output:
The sink component nodes (or "safe nodes"), in numerical order.

ex. <br>
0 2 4

