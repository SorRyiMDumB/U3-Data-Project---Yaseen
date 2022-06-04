#bruh
import graphing
import networkx as nx

G = nx.Graph()

graphing.addnodes(G)
graphing.defultgraph(G)

visted = set()

def dfs(visted , graph, node):
    if node not in visted:
            print(node)
            visted.add(node)
            
            for neighbour in graph[node]:
                dfs(visted,graph, neighbour)

dfs(visted, G, 1)

