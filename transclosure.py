#bruh
import graphing
import networkx as nx

G = nx.Graph()

graphing.addnodes(G)
graphing.defultgraph(G)


def transclosure(GROPH):
    adj = ((nx.adjacency_matrix(GROPH, dtype=None, weight='weight')).toarray()).tolist()
    nl = []
    for a in adj:
        nnl = []
        for b in a:
            #print(b)
            if b >= 1:
                b = 1
                nnl.append(b)
            else:
                nnl.append(b)
        nl.append(nnl)
    
    print("INPUT MATRIX")
    print(nl)

    def trans(adj, GROPH):
        out = [i[:] for i in adj]
        vert = GROPH.number_of_nodes()

        for k in range(vert):
            for i in range(vert):
                for j in range(vert):
                    out[i][j] = out[i][j] or (out[i][k] and out[k][j])
        return out


    #print(list(NdW.edges(data=True)))
    print("\nOUTPUT MATRIX")
    for i in trans(nl, GROPH): 
        print(i)

transclosure(G)