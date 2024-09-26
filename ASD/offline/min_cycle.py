#najkrotszy cykl w grafie ważonym
#usuwamy krawedz, szukamy najkrotszej sciezki miedzy tymi dwoma wierzcholkami i zapisujemy, usuwamy nastepna krawedz itd

from queue import PriorityQueue
def min_cycle(G):
    def restore_path(parent,start,end):
        i = end
        path = []
        while i != start:
            path.append(i)
            i = parent[i]
        path.append(start)
        path.reverse()
        return path
    def dijkstra(start,end):
        def relax(u,v,weight):
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                parent[v] = u
                return True
            return False
        q = PriorityQueue()
        dist = [float('inf') for _ in range (len(G))]
        dist[start] = 0
        parent = [None for i in range (len(G))]
        q.put((0,start))
        visited = [False]*(len(G))
        while not q.empty():
            v = q.get()[1]
            if not visited[v]:
                for j in range (N):
                    if G[v][j] != -1:
                        if relax(v,j,G[v][j]):
                            q.put((dist[j],j))
        return dist[end],parent

                       
    mini = float('inf')
    mini_path = []
    N = len(G)
    for i in range (N):
        for j in range (i+1): #wystarczy przegladnac macierz trojkątną
            if G[i][j] != -1:
                start = i
                end = j
                save = G[i][j]
                G[i][j] = -1
                dist,parent = dijkstra(i,j)
                if mini > dist + save:
                    mini_path = restore_path(parent,start,end)
                G[i][j] = save
    return mini_path



G = [[-1,2,-1,-1,1],[2,-1,4,1,-1],[-1,4,-1,5,-1],[-1,1,5,-1,3],[1,-1,-1,3,-1]]
print(min_cycle(G))