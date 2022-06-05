from math import dist
import graphing
import networkx as nx

G = nx.Graph()

graphing.addnodes(G)
graphing.defultgraph(G)

visted = []
unvisted = []

def dijkstra(GROPH, start, end):
    global visted
    global unvisted

    shortest_distance_from_start = {node: float('inf') for node in list(nx.nodes(GROPH))}
    previous_vertex = {node: None for node in list(nx.nodes(GROPH))}

    for node in GROPH:
        unvisted.append(node)

    #print(shortest_distance_from_start)
    shortest_distance_from_start[start] = 0
    current = start
    neighbours_of_current = list(GROPH.neighbors(current))

    for comrade in neighbours_of_current:
        comrade_weight = G[current][comrade]["weight"]
        preexisting_weight = shortest_distance_from_start[comrade]
        #print(comrade_weight, preexisting_weight)
        
        if comrade_weight < preexisting_weight:
            shortest_distance_from_start[comrade] = comrade_weight
            previous_vertex[comrade] = current
    
    visted.append(current)
    
    #while len(visted) < len(unvisted):
    for a in shortest_distance_from_start:
        weight = shortest_distance_from_start[a]
        print(a, weight)
    
    pass


dijkstra(G,1,2)

#https://www.youtube.com/watch?v=pVfj6mxhdMw
