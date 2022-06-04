from numpy import source
import graphing
import networkx as nx

G = nx.Graph()

graphing.addnodes(G)
graphing.defultgraph(G)

#print(nx.dijkstra_path(G,1,4))


from queue import PriorityQueue

def dijkstra(graph: 'networkx.classes.graph.Graph', start: str, end: str):
    def distance(u, v):
        return graph.get_edge_data(u, v).get('weight')
        
    prev = {}
    dist = {v: float('inf') for v in list(nx.nodes(graph))}
    visited = set()
    pq = PriorityQueue()
    
    dist[start] = 0
    pq.put((dist[start], start))
    
    while not pq.empty():
        curr_cost, curr = pq.get()
        visited.add(curr)
        print(f'visiting {curr}')
        for neighbor in dict(graph.adjacency()).get(curr):
            path = dist[curr] + distance(curr, neighbor)
            if path < dist[neighbor]:
                dist[neighbor] = path
                prev[neighbor] = curr
                if neighbor not in visited:
                    visited.add(neighbor)
                    pq.put((dist[neighbor], neighbor))
                else:
                    pq.get((dist[neighbor], neighbor))
                    pq.put((dist[neighbor], neighbor))


dijkstra(G, 1,2)