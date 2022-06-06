import graphing
import networkx as nx

G = nx.Graph()

graphing.addnodes(G)
graphing.defultgraph(G)



mst = []                        # Creates a list that contains the Minimum Spanning Tree in form of edges
mst_nodes = set()       # Creates a set that contains the nodes in the MST
mst_nodes.add(1)        # Places the node 1 into the starting nodes

low_edge = None         # Varible that contains the lowest edge


def prims(GROPH):           # Function for Prim's Algorithim
        global mst_nodes      # Allows the function to access the mst nodes
        global mst                 # Allows the function to access the mst
        global low_edge        # Allows the function to access the lowest edge
        
        edges = []                 # Creates an list that contains edges that connect to nodes in the mst

        for nodes in mst_nodes:             # Iterates through all the nodes in the mst 
            a = GROPH.edges(nodes)        # Finds the edges assoicated with the node
            for x in a:
                edges.append(x)                 # Adds edges to the edges list

        weight_and_edge = []                # Creates a list Weight And Edge is a list that contains the edges + their weights in
                                                         # in the form of a tuple (weight, [node 1 , node 2]) (also refered to as the data list)
        
        for e in edges:                             # Iterates through the edges in edges 
            u = e[0]                                    # Sets the inital node
            v = e[1]                                    # Sets the final node
            
            weight = int(GROPH[u][v]["weight"])             # finds the weight assoicated with the edge

            liste = [u, v]                                                   # Creates a list that contains the intial node and final node
            data = tuple( (int(weight), list(liste)) )          # Creates the data that contains the weight plus the inital and final nodes
            weight_and_edge.append(data)                    # Add the data to the wieghts and edge list

        a = weight_and_edge[0]                                   # Gets the intial data in the weights and edge list
        
        if len(mst) == 0:                                               # If the mst is empty 
            low_edge = a                                                # Set the lowest edge to first node in weights and edge list

        else:                                                                # If the mst is not empty
            for i in mst:                                                # Iterate through edges in the mst
                weight_and_edge.remove(i)                   # Remove the edges in the mst from the weights and edge list
            
            low_edge = weight_and_edge[0]               # Set the lowest edge to the inital value in weights and edges

        for edges in weight_and_edge:                   # Iterates through the edges in the data list
            if low_edge == edges:                             # If the lowest edge is the same as the edge 
                pass                                                    # Pass
            
            else:                                                       # If the lowest edge is diffrent to edge
                if low_edge[0] <= edges[0]:                # Check if the lowest edge weight is smaller
                    pass                                                # Retain the lowest value
                
                else:                                                   # If the lowest edge weight is larger
                    low_edge = edges                           # Make the lowest edge the new edge 

        mst.append(tuple(low_edge))                     # Add the lowest edge to the mst
        cheese = low_edge[1]                                # Add both nodes of edge into the list of mst nodes
        mst_nodes.add(cheese[0])
        mst_nodes.add(cheese[1])




print("\n\n PRIMS \n")
while len(mst_nodes) < G.number_of_nodes():         # Repeat Prims until the amount of nodes in the mst is equal to the graph 
    prims(G)
    print(len(mst_nodes))

print(mst)                  # Outputs a list that contains edges in the mst




T = nx.Graph()
for i in mst:
    uv = i[1]
    T.add_edge(uv[0], uv[1])

#graphing.drawgraph(T)
