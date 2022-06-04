import graphing
import networkx as nx

G = nx.Graph()

graphing.addnodes(G)
graphing.defultgraph(G)

length, path = nx.single_source_bellman_ford(G, 1)

print(length)
print(path)