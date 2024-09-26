import networkx as nx
import matplotlib.pyplot as plt

def rysuj_graf(graf):
    G = nx.Graph()
    for i, krawedzie in enumerate(graf):
        for krawedz in krawedzie:
            G.add_edge(i, krawedz)

    pos = nx.spring_layout(G)  # układ wierzchołków
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500, font_size=12)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Graf z wagami")
    plt.show()



def mosty(G):
    visited = [False]*(len(G))
    time = 0
    d = [0]*(len(G))
    low = [float('inf')]*(len(G))
    parent = [None]*(len(G))
    def DFSVisit(i):
        nonlocal time
        visited[i] = True
        time += 1
        d[i] = time
        low[i] = d[i]
        for v in (G[i]):
            if not visited[v]:
                parent[v] = i
                low[i] = min(DFSVisit(v),low[i])
            elif v != parent[i]: #wsteczna (czyli nie rodzic)
                low[i] = min(d[v],low[i])
        return low[i]
    DFSVisit(0) 
    print(low)
    print(d)
    for i in range(len(G)):
        if low[i] == d[i] and parent[i] != None:
            print(parent[i],"<->",i,end = ' ')
            print()
G1 = [[1,2],[0,2],[0,1,3],[2,5,4],[3,5],[3,4]]
# G2 = [[1,2],[0,2],[0,1,3],[2,5,4],[3,5,6],[3,4],[4,7,8],[6,8],[6,7]]
def convert(edges):
    max_vertice = 0
    for edge in edges:
        max_vertice = max(edge[0],edge[1],max_vertice)
    G = [[] for _ in range (max_vertice+1)]
    for edge in edges:
        G[edge[0]].append(edge[1])
        G[edge[1]].append(edge[0])
    return G
G2 = convert([[1,3],[3,4],[1,5],[3,5],[2,3]])
rysuj_graf(G2)
mosty(G1)


