#O(VE^2)
from queue import Queue

# def create_residual(N, capacity): #no w zasadzie to kopiuje capacity
#     R = [[0] * N for _ in range(N)]
#     for i in range(N):
#         for j in range(N):
#             R[i][j] = capacity[i][j]
#             R[j][i] = capacity[j][i]  # Ustawiamy odwrotne krawędzie na tę samą wartość
#     return R

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




graph = [[0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]]

print(edmonds_karp(graph,0,5))