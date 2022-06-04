
import graphing
import networkx as nx
from networkx.algorithms import *
from queue import PriorityQueue
from random import randint, uniform
import matplotlib.pyplot as plt

from random import choice


LENGTH = 10 # Number of iterations required to fill pbar

G = nx.Graph()

graphing.addnodes(G)
graphing.defultgraph(G)

mst = []
mst_nodes = set()
mst_nodes.add(1)
mst_nodes.add(2)

low_edge = None
def prims(GROPH):
        global mst_nodes

    #while len(mst_nodes) < GROPH.number_of_nodes():
        #startnode = choice(list(GROPH.nodes()))

        global mst
        
        global low_edge
        # edges is a list containing edges that connect to nodes in the mst
        edges = []

        for nodes in mst_nodes:
            a = GROPH.edges(nodes)
            for x in a:
                edges.append(x)
        
        #print("\n Edges connecting to ", mst_nodes, "\n", edges, "\n")
        
        # weight and edge is a list that contains the edges + their weights in
        # in the form of a tuple (weight, [node 1 , node 2])
        weight_and_edge = []
        
        for e in edges:
            u = e[0]
            v = e[1]
            weight = int(GROPH[u][v]["weight"])

            liste = [u, v]
            data = tuple( (int(weight), list(liste)) )
            weight_and_edge.append(data)

        #print("#######weights and edge", weight_and_edge[0])
        #print("mst",mst)
        

        a = weight_and_edge[0]
        
        if len(mst) == 0:
            low_edge = a
            #print("mst is empty")

        else:
            #print("mst is not empty")

            for i in mst:
                #print(i)
                weight_and_edge.remove(i)
            
            low_edge = weight_and_edge[0]
            

        #print("intial edge",low_edge)





        for edges in weight_and_edge:
            #print("comparing lowedge", low_edge, "to edge ", edges)
            
            if low_edge == edges:
                #print("same node")
                pass
            
            else:
                if low_edge[0] <= edges[0]:
                    #print("low edge is smaller")
                    pass
                
                else:
                    #print(edges)
                    low_edge = edges
                    #print("new lowedge")

        #print("lowest edge found\n",low_edge)

        mst.append(tuple(low_edge))
        
        cheese = low_edge[1]
        mst_nodes.add(cheese[0])
        mst_nodes.add(cheese[1])

        #print(mst)
        #print(mst_nodes)



print("\n\n PRIMS \n")


while len(mst_nodes) < G.number_of_nodes():
    prims(G)
    print(len(mst_nodes))



"""
prims(G)
prims(G)
prims(G)
prims(G)
prims(G)
prims(G)
prims(G)

if len(mst_nodes) < G.number_of_nodes():
    print("less")
    print(len(mst_nodes))

"""
