#bruh
import graphing
import networkx as nx

G = nx.Graph()

graphing.addnodes(G)
graphing.defultgraph(G)


def transclosure(GROPH):           # Function for Transitive closure 
    adj = ((nx.adjacency_matrix(GROPH, dtype=None, weight='weight')).toarray()).tolist()       # Creates an adjacency matrix for all nodes in Graph
    print("INPUT MATRIX")
    print(adj)                                          # Outputs input matrix

    def trans(adj, GROPH):                              # Creates a repeated process called trans
        out = [i[:] for i in adj]                             # Creates a list that contains all the nodes adjacencies 
        vert = GROPH.number_of_nodes()          # Retrieves the number of nodes in Graph

        for k in range(vert):                                                           # iterates through amount of nodes in Graph
            for i in range(vert):                                                        # iterates through amount of nodes in Graph
                for j in range(vert):                                                   # iterates through amount of nodes in Graph
                    out[i][j] = out[i][j] or (out[i][k] and out[k][j])        # If vertex k is on a path from i to j, then make sure that the value of reach[i][j] is 1
        return out                                                                          # Output if able to reach


    #print(list(NdW.edges(data=True)))
    print("\nOUTPUT MATRIX")
    for i in trans(adj, GROPH): 
        print(i)

transclosure(G)