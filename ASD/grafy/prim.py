from queue import PriorityQueue
def prim(G,start):
    A = [False]*(len(G)) 
    weights = [float('inf')]*(len(G))   #najtansze polaczenie do i-tego wierzcholka
    q = PriorityQueue()
    q.put((0,start))
    weights[start] = 0 
    parent = [None]*(len(G))
    cost = 0
    while not q.empty():
        w,u = q.get()
        if A[u]:
            continue
        A[u] = True
        cost += w
        for i,weight in G[u]:
            if not A[i] and weights[i] > weight: #tutaj znaczaca roznica z dijkstrą. w dijkstrze dodajemy czesto te same elementy do kolejki (bo mogly byc zrelaksowane)
                weights[i] = weight
                q.put((weight,i))
                parent[i] = u
                    
    MST = []
    for i in range (len(G)):
        if parent[i] != None:
            MST.append((parent[i],i))
    return MST

G1 = [
    [(1, 2), (3, 6)],
    [(0, 2), (2, 3), (3, 8), (4, 5)],
    [(1, 3), (4, 7)],
    [(0, 6), (1, 8), (4, 9)],
    [(1, 5), (2, 7), (3, 9)]
]

G2 = [
    [(1, 1), (2, 4)],
    [(0, 1), (2, 2), (3, 6)],
    [(0, 4), (1, 2), (3, 3)],
    [(1, 6), (2, 3)]
]

G3 = [
    [(1, 3), (2, 1)],
    [(0, 3), (2, 7), (3, 5), (4, 1)],
    [(0, 1), (1, 7), (4, 3)],
    [(1, 5), (4, 6), (5, 2)],
    [(1, 1), (2, 3), (3, 6), (5, 4)],
    [(3, 2), (4, 4)]
]



print(prim(G3,0))