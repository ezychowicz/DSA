import networkx as nx
import matplotlib.pyplot as plt
import random
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
def punkty_artykulacji(G):
    visited = [False]*(len(G))
    d = [float('inf')]*(len(G))
    time = 0
    low = [float('inf')]*(len(G))
    parent = [None]*(len(G))
    points = []
    def DFSVisit(i):
        nonlocal time,points
        visited[i] = True
        time += 1
        d[i] = time
        low[i] = d[i]
        children = 0
        flag = False
        for v in G[i]:
            if not visited[v]:
                children += 1
                parent[v] = i
                DFSVisit(v)
                low[i] = min(low[i],low[v])
                if parent[i] != None and not flag and low[v] >= d[i]: 
                    points.append(i) 
                    flag = True
            elif parent[i] != v:
                low[i] = min(low[i],d[v])

                  
        if children > 1 and parent[i] == None:
            points.append(i)
    
    DFSVisit(0)
    return points
G1 = [[1,2],[0,2],[0,1,3],[2,5,4],[3,5],[3,4]]

G2 = [[1,2],[0,2],[0,1,3],[2,5,4],[3,5,6],[3,4],[4,7,8],[6,8],[6,7]]
G3 = [[1, 12, 7, 15, 6, 2, 43, 23], [5, 30, 0, 35, 29, 3, 48, 41, 17], [20, 37, 32, 8, 41, 43, 0, 4, 18], [41, 1, 29, 16, 7, 33, 6], [9, 43, 20, 33, 11, 41, 12, 30, 2], [1, 9], [0, 39, 3, 45], [19, 0, 9, 11, 3, 12], [14, 11, 22, 2, 25, 40, 10, 30], [4, 7, 5, 12, 48, 13, 27, 21, 11], [13, 8], [16, 38, 8, 7, 18, 4, 30, 9], [0, 19, 27, 9, 21, 26, 4, 29, 7], [44, 10, 34, 24, 22, 33, 25, 16, 9, 27, 23], [8, 34, 37, 39], [42, 0, 38, 35, 23], [11, 31, 38, 24, 13, 3], [26, 43, 18, 1], [48, 28, 11, 40, 17, 26, 2, 34], [7, 31, 35, 12, 46], [2, 4, 26, 39, 47], [46, 12, 36, 33, 9, 22, 40], [8, 13, 21], [42, 48, 38, 0, 15, 13, 39], [33, 49, 16, 13, 28], [43, 8, 13, 37, 44], [42, 17, 20, 12, 18], [40, 12, 9, 13, 49], [18, 34, 24], [40, 1, 12, 3], [41, 1, 43, 49, 32, 11, 4, 8], [39, 19, 16, 35], [2, 30], [24, 46, 4, 13, 21, 3, 45], [28, 14, 13, 45, 42, 18], [1, 19, 31, 15], [21], [2, 14, 25], [11, 16, 23, 15], [31, 44, 14, 20, 6, 46, 23], [43, 27, 29, 18, 8, 21], [30, 3, 4, 1, 2], [15, 26, 23, 46, 34], [30, 40, 25, 4, 17, 2, 0], [13, 39, 45, 25], [44, 34, 46, 6, 47, 33], [33, 21, 19, 45, 42, 39], [48, 45, 20], [18, 23, 47, 1, 9], [24, 30, 27]]

print(punkty_artykulacji(G3))
