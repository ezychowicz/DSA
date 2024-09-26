#zad kolos - ale de facto znalezc najwieksze skojarzenie w grafie dwudzielnym (max ilosc par)
from queue import Queue
def edmonds_karp(capacity, s, t):
    def bfs(s,t):
        nonlocal parent
        visited = [False]*(len(R))
        q = Queue()
        increase = 0 #zmiana flow w tej rundzie
        q.put((s,float('inf')))
        visited[s] = True
        parent = [None]*(len(R))
        while not q.empty():
            v,v_flow = q.get()
            for i in range (len(R[v])):
                if not visited[i] and R[v][i] != 0:
                    parent[i] = v
                    increase = min(v_flow, R[v][i])
                    visited[i] = True
                    q.put((i, increase))
                    if i == t:
                        return increase
        return 0
    
    def update_residual(R, parent, growth):
        i = t 
        while parent[i] != None:
            R[parent[i]][i] -= growth
            R[i][parent[i]] += growth
            i = parent[i]
        

    N = len(capacity)
    R = capacity[::] #aktualnie wszystko jest dla flow = 0
    flow = 0
    parent = [None]*(len(R))
    growth =  bfs(s,t) 
    
    while growth != 0:  #dopoki udaje sie znalezc sciezke powiekszajaca
        flow += growth
        update_residual(R, parent, growth)
        growth = bfs(s,t)

    return flow



def floyd_warshall(G): 
    N = len(G)
    dist = [[float('inf') for _ in range (N)] for __ in range (N)]  
    for i in range (N):  
        for j in range (len(G[i])):
            if G[i][j] != 0:
                dist[i][j] = G[i][j]
  
    for i in range (N):  
        dist[i][i] = 0
    
    for k in range (N):  
        for x in range (N):
            for y in range (N):
                if dist[x][k] + dist[k][y] < dist[x][y]:
                    dist[x][y] = dist[x][k] + dist[k][y]
    return dist        


def create_graph(G,K,D): #graf,kolor,min_dist
    dist = floyd_warshall(G)
    bipart = [[0 for __ in range (len(G) + 2)] for _ in range (len(G) + 2)]
    for i in range (len(G)):
        for j in range (len(G)):
            if dist[i][j] >= D and K[i] != K[j] and K[i] == "G": #krawedzie są skierowane od G do B
                bipart[i + 2][j + 2] = 1
    for i in range (len(G)):
        if K[i] == "G":
            bipart[0][i + 2] = 1 #wiezrcholek t polaczony z wierzcholkami G
        else:
            bipart[i + 2][1] = 1 #wierzcholki B polaczone z wierzcholkiem t
    return bipart
def skojarzenie(G,K,D):
    bipart = create_graph(G,K,D) #D-graf dwudzielny skierowany z dodatkowymi wierzcholkami s i t
    return edmonds_karp(bipart, 0, 1)

G = [
[0, 1, 1, 0, 1],
[1, 0, 0, 1, 0],
[1, 0, 0, 0, 1],
[0, 1, 0, 0, 1],
[1, 0, 1, 1, 0],
]
K = ['B', 'B', 'G', 'G', 'B']
D = 2
print(skojarzenie(G,K,D))