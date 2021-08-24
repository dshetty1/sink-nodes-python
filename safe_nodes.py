#Name: Dhruv Shetty

import sys

sys.setrecursionlimit(10000)


### THE BELOW 2 DATA STRUCTURES ARE NOT MY CODE (Graph and DFSINnfo)


# Data structure for representing a graph
class Graph():

    # Initalize a graph with n vertices and no edges
    def __init__(self, n):

        # Number of nodes in the graph
        self.n = n
        
        # For u in [0..n), A[u] is the adjacency list for u
        self.A = [[] for i in range(n)]

    # Add an edge u -> v to the graph
    def add_edge(self, u, v):
        self.A[u].append(v)

# Data structure holding data computed by DFS
class DFSInfo():
    def __init__(self, graph):

        # Number of nodes in graph
        n = graph.n

        # Number of trees in DFS forest
        self.k = 0           

        # For u in [0..n), T[u] is initally 0, but when DFS discovers u, T[u] is set to the
        # index (which is in [1..k]) of the tree in DFS forest in which u belongs.
        self.T = [0 for i in range(n)]  

        # List of nodes in order of decreasing finish time           
        self.L = [-1 for i in range(n)] 

        # initially set to n, and is decremented every time DFS finishes with a node and is recorded in L                    
        self.count = n                  

# Performs a recursive DFS, starting at u
def rec_DFS(u, graph, dfs_info):

    # Add to component index
    dfs_info.T[u] = dfs_info.k

    for v in (graph.A[u]):
        if dfs_info.T[v] == 0:
            rec_DFS(v, graph, dfs_info)

    # Decrement count by 1 and add node to array L (lists of nodes in order of decreasing finish time)
    dfs_info.count -= 1
    dfs_info.L[dfs_info.count] = u

# Performs a larger DFS on given graph in the order specified.
# Returns DFSInfo object (outlined above)
def DFS(order, graph):

    d_info = DFSInfo(graph)

    for v in order:
        if d_info.T[v] == 0:
            d_info.k += 1
            rec_DFS(v, graph, d_info)


    return d_info

# Returns a boolean array indicating which nodes are in sink components.
def compute_safe_nodes(graph, dfs_info):

    # Initialize boolean array
    bool_arr = []
    for i in range(dfs_info.k+1):
        bool_arr.append(True)

    # If a node has nodes in its' a adjacency list which do not lie in the same SCC component as
    # the original node, that node is not in a sink component (its' component has outward edges)
    for j in range(graph.n):
        for x in graph.A[j]:
            if dfs_info.T[j] != dfs_info.T[x]:
                bool_arr[dfs_info.T[j]] = False
                break

    # If a node's SCC component is a sink, add that node to the safe_nodes array
    safe_nodes = []
    for j in range(graph.n):
        if bool_arr[dfs_info.T[j]] == True:
            safe_nodes.append(j)

    return safe_nodes


# Returns the reverse of the given graph (Transpose(G) or the transpose of the graph) (i.e. edges are reversed)
def reverse(graph):
    reverse_g = Graph(graph.n)

    index = 0

    # Reverses edges in the original graph
    for i in graph.A:
        for x in range(len(i)):
            if len(i) == 0:
                continue
            else:
                starting_node = i[x]
                destination_node = index
                reverse_g.add_edge(starting_node, destination_node)
        index += 1
        
    return reverse_g


if __name__ == "__main__":

    # Code for standard line input rather than text file
    '''
    inputs = input()
    intersections = int(inputs.split()[0])
    streets = int(inputs.split()[1])
    
    
    g = Graph(intersections)

    while streets > 0:
        inputs = input()

        starting_node = int(inputs.split()[0])
        destination_node = int(inputs.split()[1])
        g.add_edge(starting_node, destination_node)

        streets -= 1
    '''


    # Code for text file input
    f = open('graph.txt', 'r')
    inputs = f.readline()

    nodes = int(inputs.split()[0])
    edges = int(inputs.split()[1])

    g = Graph(nodes)

    while edges > 0:
        inputs = f.readline()

        starting_node = int(inputs.split()[0])
        destination_node = int(inputs.split()[1])
        g.add_edge(starting_node, destination_node)

        edges -= 1

    '''
    Kosaraju Algorithm:
      1. Compute reverse of original graph --> (G^T)
      2. Call DFS(G^T), and order nodes (v1, ... , vn) in order of decreasing finishing time
      3. Call DFS (G), but in the top-level loop process in the order above (v1, ... , vn).
    The trees in the DFS forest are the SCC's of G
    '''

    # Step 1.
    rev_g = reverse(g)

    order_arr = []
    for i in range(g.n):
        order_arr.append(i)

    # Step 2.
    info_rev = DFS(order_arr, rev_g)

    # Step 3.
    info_SCC = DFS(info_rev.L, g) 

    # Compute nodes in sinks from SCC graph of the original graph
    result = compute_safe_nodes(g, info_SCC)

    # Print "safe nodes" to the output
    for i in result:
        print(i, end = " ")