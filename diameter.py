import graphing
import networkx as nx

G = nx.Graph()

graphing.addnodes(G)
graphing.defultgraph(G)

def diameter(GROPH):
    for u in GROPH:
        for v in GROPH:
            print(u,v)
            

diameter(G)