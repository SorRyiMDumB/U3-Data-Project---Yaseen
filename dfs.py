#bruh
import graphing
import networkx as nx

G = nx.Graph()

graphing.addnodes(G)
graphing.defultgraph(G)

visted = set()          # Creates a list/set for the visited nodes

def dfs(visted , graph, node):       # Function for Breadth First Search
    if node not in visted:                 # Check if the node is not in the visited 
            print(node)                        # Print the node
            visted.add(node)                # Add the node to the visited set
            
            for neighbour in graph[node]:           # Iterate through all the neighbours of the node
                dfs(visted,graph, neighbour)        # Recurse through the DFS algorithim with the neighbour

dfs(visted, G, 1)

