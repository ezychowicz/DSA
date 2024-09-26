from queue import PriorityQueue


def dijkstra(G,x):
    def relax(u,v,edge_w):
        if dist[u] + edge_w < dist[v]:
            dist[v] = dist[u] + edge_w
            parent[v] = u
            return True
        return False
    heap = PriorityQueue()
    dist = [float('inf')]*(len(G))
    dist[x] = 0
    heap.put((dist[x],x))
    parent = [None]*(len(G))
    visited = [False]*(len(G))
    while not heap.empty():
        k = heap.get()
        if visited[k[1]]: #odnosi sie do sytuacji gdy podczas jednej "fali" dodamy jeden wierzcholek dwa razy (najpierw z wiekszym dist, potem z mniejszym (relax dwa razy)), wtedy liczy sie tylko ten drugi raz, a na kopcu zostanie też ten pierwszy
            continue
        visited[k[1]] = True
        for v in G[k[1]]:
            if relax(k[1],v[0],v[1]):  #moze byc jeszcze 'not visited[v[0]]', bo jak odwiedzone to juz ustalone w sumie i na pewno relax bedzie false
                heap.put((dist[v[0]],v[0]))
    return dist,parent
def find_path(parent,dest,x):
    i = dest
    path = []
    while i != x:
        path.append(i)
        i = parent[i]
    path.reverse()
    return path
G = [[(1,2),(6,1)],[(0,2),(7,1),(2,7)],[(1,7),(7,1),(3,4)],[(2,4),(7,8),(4,1)],[(3,1),(5,5)],[(6,2),(7,2),(4,5)],[(5,2),(7,3),(0,1)],[(6,3),(5,2),(3,8),(2,1),(1,1)]]

print(dijkstra(G,0))

dest = 4
import time
start = time.time()
for i in range (100000):
    #print("sciezka do ",dest,":",find_path(dijkstra(G,0)[1],dest,0))
    find_path(dijkstra(G,0)[1],dest,0)
end = time.time()
print(end-start)
