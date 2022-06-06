import graphing
import networkx as nx

G = nx.Graph()

graphing.addnodes(G)
graphing.defultgraph(G)


visited = []      # List for visited nodes.
queue = []      # Initialize a queue

def bfs(visited, GROPH, node):       # Function for Breadth First Search
  visited.append(node)                  # Add the starting node to the visited list
  queue.append(node)                   # Add the starting node to the queue

  while queue:                              # Creating loop to visit each node
    m = queue.pop(0)                     # Assign the first value of the queue to m
    print(m, end = ", ")                  # Print out m 
    

    for neighbour in GROPH[m]:      # Iterates through the neighbours of m
      if neighbour not in visited:      # If the neighbour is not found in visted list ie. the node has not been visited yet
        visited.append(neighbour)     # Adds the neighbour node to the visited list
        queue.append(neighbour)       # Adds the neighbour node to the queue

print("\n\n Breadth First Search results starting at node '1'\n")

bfs(visited, G, 1)



#graphing.drawgraph(G)