import networkx 
def bellman_ford(G,start,dest):
    def relax(u,v,weight):
        if dist[u] + weight < dist[v]:
            dist[v] = dist[u] + weight
            parent[v] = u
    def restore_path(parent,dest):
        i = dest
        path = []
        while i != start:
            path.append(i)
            i = parent[i]
        path.append(start)
        path.reverse()
        return path 
    
    parent = [None]*(len(G))
    dist = [float('inf')]*(len(G))
    dist[start] = 0
    for _ in range (len(G)-1):
        for u in range (len(G)):
            for v,w in G[u]:
                relax(u,v,w)
    print(dist)
    for i in range (len(G)):
        for v,w in G[i]:
            if dist[i] + w < dist[v]:
                print(i,v)
                return False
    return restore_path(parent,dest)
graf = [[(1,1)],[(3,3),(2,-5)],[(5,10)],[(2,4),(4,-1)],[(0,2)],[(3,3),(0,-1),(4,2)]]
graf = [[(1,1)],[(2,-5)],[(5,10)],[(5,15),(2,4),(4,-1),(1,1)],[(0,2)],[(0,-1),(4,2)]]
import networkx as nx
import matplotlib.pyplot as plt
import random

def rysuj_graf(graf):
    G = nx.DiGraph()
    for i, krawedzie in enumerate(graf):
        for krawedz in krawedzie:
            G.add_edge(i, krawedz[0], weight=krawedz[1])

    pos = nx.spring_layout(G)  # układ wierzchołków
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500, font_size=12)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=15)
    plt.title("Graf z wagami")
    plt.show()

# Rysowanie grafu z wagami
# print("Graf 1 z losowymi wagami:")
# print(bellman_ford(graf,0,3))
rysuj_graf(graf)


