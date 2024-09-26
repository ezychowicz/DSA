import networkx as nx
import matplotlib.pyplot as plt
import random
def rysuj_graf(graf):
    G = nx.Graph()
    for i, krawedzie in enumerate(graf):
        for krawedz in krawedzie:
            G.add_edge(i, krawedz[0], weight=krawedz[1])

    pos = nx.spring_layout(G)  # układ wierzchołków
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500, font_size=12)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Graf z wagami")
    plt.show()

def List_to_matrix(G, weighted = False, zeros = True): # from list of lists G to matrix H
    if zeros:
        H = [[0 for __ in range(len(G))] for _ in range(len(G))]
    else:
        H = [[float('inf') for _ in range(len(G))] for __ in range(len(G))]
    if not weighted:
        for v, edges in enumerate(G):
            for u in edges:
                H[v][u] = 1
    else:
        for v, edges in enumerate(G):
            for u, weight in edges:
                H[v][u] = weight
    return H
#istnienie sciezki hamiltona w DAGu, macierz sasiedztwa O(V), lista sasiedztwa O(V*E) bo zeby sprawdzic czy dwa wierzcholki są sąsiadami przeszukujemy wszystkich sąsiadow v1/v2
def Hamilton_DAG(G):
    def topological_sort(G):
        visited = [False]*(len(G))
        order = [None]*(len(G))
        cnt = len(G) - 1
        def DFSVisit(i):
            nonlocal cnt
            visited[i] = True
            for v in range (len(G)):
                if G[i][v] and not visited[v]:
                    DFSVisit(v)
            order[cnt] = i
            cnt -= 1
        for u in range (len(G)):
            if not visited[u]:
                DFSVisit(u)
        return order
    
    order = topological_sort(G)
    for i in range (1,len(G)):
        if not G[order[i-1]][order[i]]:
            return False
    return True

#dobry poczatek - wierzcholek w DG z ktorego mozna dojsc do kazdego innego wierzcholka w grafie
#brute: O(V(V+E)) - DFS dla kazdego wierzcholka i czy da sie dojsc do kazdego (is_connected w zasadzie) 
#O(V+E): 1) SCC 2) DFS od pierwszej skladowej, czy pierwsza skladowa polaczona z kazda inną
#optimal O(V+E): 1) DFS i znaleźć wierzchołek o najwiekszym czasie przetworzenia. 2)puścić z niego DFS 
def DFS_order(G):
    visited = [False]*(len(G))
    order = [None]*(len(G))
    cnt = len(G) - 1
    def DFSVisit1(i):
        nonlocal cnt
        visited[i] = True
        for v in range (len(G)):
            if G[i][v] and not visited[v]:
                DFSVisit1(v)
        order[cnt] = i
        cnt -= 1
    for u in range (len(G)):
        if not visited[u]:
            DFSVisit1(u)
    return order

def translate(G):
    G_T = [[0 for _ in range(len(G))] for __ in range (len(G))]
    for i in range (len(G)):
        for j in range (len(G)):
            if G[i][j] == 1:
                G_T[j][i] = 1
    return G_T

def SCC_graph(G):

    order = DFS_order(G)
    G_T = translate(G)
    visited = [-1]*(len(G))
    comp = 0
    SCC = [] #bedzie to lista sasiedztwa grafu SCC
    def DFSVisit(i,comp):
        visited[i] = comp
        for v in range(len(G_T[i])):
            #print(G_T[i][v],visited[v],comp)
            if G_T[i][v] == 1 and visited[v] == -1:
                DFSVisit(v,comp) 
            elif G_T[i][v] == 1 and visited[v] != comp:
                if comp not in SCC[visited[v]]:
                    SCC[visited[v]].append(comp)

    for v in order:
        if visited[v] == -1:
            DFSVisit(v,comp)
            comp += 1
            SCC.append([])
    print(SCC,visited)
    visited = [False]*(len(SCC))
    def DFSVisit_SCC(i):
        visited[i] = True
        for v in SCC[i]:
            if not visited[v]:
                DFSVisit_SCC(v)
    
    DFSVisit_SCC(0)
    if False in visited:
        return False
    return True

def optimal(G):
    visited = [False]*(len(G))
    last = -1
    def DFSVisit_optimal(i):
        nonlocal last
        visited[i] = True
        for v in range (len(G)):
            if G[i][v] and not visited[v]:
                DFSVisit_optimal(v)
        last = i
    def DFSVisit(i):
        visited[i] = True
        for v in range (len(G)):
            if G[i][v] and not visited[v]:
                DFSVisit(v)
    for v in range (len(G)):
        if not visited[v]:
            DFSVisit_optimal(v)
    visited = [False]*(len(G))
    DFSVisit(last)
    if False in visited:
        return False
    return True

# G = List_to_matrix([[1],[2,4,7],[3],[0],[6],[6],[],[1,6]])

# print(optimal(G),SCC_graph(G))

#czy mozna usunac krawedz nalezaca do najkrotszej sciezki w taki sposob, aby dist(x,y) sie nie zmienil
import queue
def bfs_count_paths(G,x,y):
    q = queue.Queue()
    visited = [0]*(len(G))
    visited[x] = 1
    q.put(x)
    dist = [0]*(len(G))
    while not q.empty():
        u = q.get()
        if u == y:
            return visited[y] #if >1 return True (>1 najkrotsza sciezka do y)
        for v in G[u]:
            if visited[v] == 0:
                visited[v] += visited[u]
                dist[v] = dist[u] + 1
                q.put(v)
            else:
                if dist[v] < dist[u] + 1: #gdy odwiedzony wierzcholek wczesniej ma najkrotsza sciezke krotszą od tej nowo wchodzacej to nie dodawaj do licznika najkrotszych sciezek
                    continue
                visited[v] += visited[u]
    return -1

#G = [[8,1,9],[2,3,0],[1,3],[1,2,4],[3,5],[4,6],[5,7,10],[6,8],[0,7],[0,10],[9,6]]
#print(bfs_count_paths(G,0,5))


#zad6
from queue import PriorityQueue
def alicja_bob(G,start,dest):    
    def restore_path(parent_a,parent_b,start,dest):
        path = []
        i = dest
        cnt = 0
        while i != start:
            path.append(i)
            if cnt%2 == 0:
                i = parent_a[i]
            else:
                i = parent_b[i]
            cnt += 1
        path.append(start)
        path.reverse()
        return path
    def dijkstra(G,start,bob_first,dest):
        visited = [[False,False] for _ in range (len(G))]
        parent_a = [None]*(len(G))
        parent_b = [None]*(len(G))
        def relax(u,v,edge_weight):
            if edge_weight == 0:
                if dist[u][0] < dist[v][1]: #0=alicja, gdy edge_w=0 to interesuje nas dist w zrodle dla alicji, a w destynacji dla boba
                    dist[v][1] = dist[u][0]  
                    parent_b[v] = u
                    return True
            else:
                if dist[u][1] + edge_weight < dist[v][0]: 
                    dist[v][0] = dist[u][1] + edge_weight  
                    parent_a[v] = u
                    return True
            return False

        heap = PriorityQueue()
        dist = [[float('inf'),float('inf')] for _ in range (len(G))]
        dist[start] = [0,0]
        heap.put((0,start,bob_first))
        while not heap.empty():
            k = heap.get()
            if visited[k[1]][k[2]]:
                continue
            visited[k[1]][k[2]] = True
            for v in G[k[1]]:
                if k[2]:
                    edge_weight = 0
                else:
                    edge_weight = v[1]
                if relax(k[1],v[0],edge_weight):
                    heap.put((dist[v[0]],v[0],not k[2]))
        return dist[dest],parent_a,parent_b
    
    bob = dijkstra(G,start,True,dest) 
    alicja = dijkstra(G,start,False,dest)
    if min(bob[0]) <= min(alicja[0]): 
        if bob[0][0] > bob[0][1]: #lepiej jak konczylismy na alicji
            path = restore_path(bob[2],bob[1],start,dest) 
        else:
            path = restore_path(bob[1],bob[2],start,dest)
        return path,"bob zaczyna",min(bob[0]) 
    else:
        if alicja[0][0] > alicja[0][1]: #lepiej jak konczylismy na alicji
            path = restore_path(alicja[2],alicja[1],start,dest) 
        else:
            path = restore_path(alicja[1],alicja[2],start,dest)
        return path,"alicja zaczyna",min(alicja[0])

graf = [[1,4,5,6],[0,4,2],[1,3],[4,2,9],[0,1,5,3],[0,4,6,7],[0,5,7],[6,5,9,8],[7,9],[3,7,8]]
def add_random_weights(G):
    for i in range (len(G)):
        for j in range (len(G[i])):
            w = random.randint(1,10)
            if type(G[i][j]) == int:
                k = G[G[i][j]].index(i)
                G[G[i][j]][k] = (G[G[i][j]][k],w)
                G[i][j] = (G[i][j],w)
    return G

graf = [[1,4,5,6],[0,(4,1000),(2,1000)],[(1,1000),3],[(4,1000),2,9],[0,(1,1000),(5,1000),(3,1000)],[0,(4,1000),6,(7,1000)],[0,5,(7,1000)],[(6,1000),(5,1000),9,8],[7,9],[3,7,8]]
        

graf = add_random_weights(graf)
print(alicja_bob(graf,0,9))
rysuj_graf(graf)
#zad7
#w kazdym wierzcholku mozemy dotankowac od 0 do D-curr. Nalezy rozwazyc kazda mozliwosc, co umozliwy tablica dwuwymiarowa cost (kazdy wierzcholek ma swoją tablice, po ktorej nawiguje sobie
#dijkstra)

# def gas_station(G,start,dest,D,market):
#     def dijkstra(G):
#         heap = PriorityQueue()
#         cost = [[float('inf') for _ in range (D+1)] for __ in range (len(G))] #w zaleznosci od tego ile paliwa mamy (od 0 do D wlacznie)
#         heap.put((0,start,D)) #koszt,aktualna pozycja,dostepne paliwo
#         cost[start][D] = 0
#         visited = [[False for _ in range (D+1)] for __ in range (len(G))]
#         parent = [[None for _ in range (D+1)] for __ in range (len(G))]
#         while not heap.empty():
#             k = heap.get()
#             if visited[k[1]][k[2]]:
#                 continue
#             visited[k[1]][k[2]] = True
#             for v in G[k[1]]:
#                 curr = k[2] - v[1] #ile paliwa po przejezdzie przez krawedz
#                 if curr < 0:
#                     continue
#                 for fuel in range (curr,D+1): #z jaka iloscia paliwa w baku wyjedziemy ze stacji
#                     price = (fuel - curr)*market[v[0]]
#                     if cost[v[0]][fuel] > cost[k[1]][k[2]] + price: #relax()
#                         cost[v[0]][fuel] = cost[k[1]][k[2]] + price
#                         parent[v[0]][fuel] = (k[1],k[2])  
#                         heap.put((cost[v[0]][fuel], v[0], fuel))
#         return parent,cost
    
#     def restore_path(cost,parent):
#         mini = float('inf')
#         fuel = -1
#         for i,c in enumerate(cost[dest]):
#             if mini > c:
#                 mini = c
#                 fuel = i
#         print(mini)
#         i = dest
#         path = []
#         while i != start:
#             path.append((i,fuel))
#             i,fuel = parent[i][fuel][0],parent[i][fuel][1]
#         path.append((i,fuel))
#         path.reverse()
#         return path
    
#     parent,cost = dijkstra(G)
#     print(parent,cost)
#     path = restore_path(cost,parent)
#     return path


# def createG(edges, n):
#     G = [ [] for _ in range(n) ]
#     for edge in edges:
#         a, b, weight = edge[0], edge[1], edge[2]
#         G[a].append( (b, weight) )
#         G[b].append( (a, weight) )
#     return G



# E = [(0, 1, 5), (1, 2, 3), (0, 2, 7), (2, 3, 4), (3, 4, 6)]
# C = [8, 5, 3, 2, 1]
# G = createG(E, 5)
# #rysuj_graf(G)
# s = 0
# t = 4
# D = 10

# #print(gas_station(G, s, t, D, C))


# E = [(0, 1, 4), (0, 7, 5), (0, 6, 8), (6, 7, 3), (1, 6, 6), (7, 8, 20), (8, 4, 9),
#      (5, 6, 12), (5, 4, 7), (1, 2, 15), (5, 2, 17), (2, 4, 10), (2, 3, 5), (4, 3, 18)]
# C = [5, 7, 3, 5, 2, 1, 8, 10, 6]
# G = createG(E, 9)
# rysuj_graf(G)
# s = 0
# t = 3
# D = 14

#print(gas_station(G, s, t, D, C))