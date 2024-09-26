from queue import PriorityQueue
def restore_from_heap(heap,k):
    ans = [None]*(k)
    for i in range (k):
        ans[-i - 1] = -heap.get()
    return ans

def dijkstra(G,x,y,k):
    def relax(u,v,weight,d):

        if vertice_q[v].empty or d + weight < abs(vertice_q[v].queue[0]): #bo zawsze optymalizujemy wzgledem ostatniego dodanego, a ostatni dodany musi byc najgorszy (tak dziala dijkstra) czyli musi byc na szczycie maxheap
            vertice_q[v].put(-(d + weight))
            q.put((d + weight, v))

    q = PriorityQueue()
    vertice_q = [PriorityQueue() for _ in range (len(G))]
    vertice_q[x].put(0)
    q.put((0,x))
    progress = [0]*(len(G)) #progress rosnie gdy bierzemy z głownej kolejki dany element, bo to oznacza ze wzielismy juz optymalny
    
    while not q.empty():
        d,u = q.get()
        # if progress[u] >= k:
        #     continue
        for v,weight in G[u]:
            relax(u,v,weight,d)
        progress[u] += 1    
        if progress[y] == k - 1:
            return restore_from_heap(vertice_q[y],k)
            

adjacency_list = [
    [],     
    [(2, 1), (3, 3)],  
    [(3, 2), (4, 6)],
    [(2, 8), (4, 1)],  
    []          
]

print(dijkstra(adjacency_list, 1, len(adjacency_list) - 1, 3))