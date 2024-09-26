import queue

def bfs(T,start): #T - lista sąsiedztwa
    visited = [False]*(len(T))
    parents = [None]*(len(T))
    distance = [None]*(len(T))
    q = queue.Queue()
    q.put(start)
    distance[start] = 0
    visited[start] = True
    #print(start,end = ' ')
    while not q.empty():
        k = q.get()
        for el in T[k]:
            if not visited[el]:
                #print(el,end = ' ')
                distance[el] = distance[k] + 1 
                parents[el] = k 
                q.put(el)
                visited[el] = True
    return distance

def is_connected(T): #czy spójny
    distance = bfs(T,0)
    for el in distance:
        if el == None:
            return False
    return True

def is_acyclic(T):
    visited = [False]*(len(T))
    parents = [None]*(len(T))
    distance = [None]*(len(T))
    q = queue.Queue()
    q.put(0)
    distance[0] = 0
    visited[0] = True
    print(0,end = ' ')
    while not q.empty():
        k = q.get()
        for el in T[k]:
            if not visited[el]:
                print(el,end = ' ')
                distance[el] = distance[k] + 1 
                parents[el] = k 
                q.put(el)
                visited[el] = True
            else:
                if parents[k] != el:
                    return False,k,el #te dwa elementy na pewno w jakims Cn
    return True

# def is_bipartite(T):  #dla spojnych
#     visited = [False]*(len(T))
#     parents = [None]*(len(T))
#     distance = [None]*(len(T))
#     q = queue.Queue()
#     q.put(0)
#     distance[0] = 0
#     visited[0] = True
#     #print(0,end = ' ')
#     while not q.empty():
#         k = q.get()
#         for el in T[k]:
#             if not visited[el]:
#                 #print(el,end = ' ')
#                 distance[el] = distance[k] + 1 
#                 parents[el] = k 
#                 q.put(el)
#                 visited[el] = True
#             else:
#                 if distance[el]%2 == 0 and (distance[k] + 1)%2 == 0:
#                     continue
#                 return False
#     return True
def dwudzielnosc(G):
    colors = [-1]*(len(G))
    def is_bipartite2(G,start): #dwukolorowanie
        q = queue.Queue()
        q.put(start)
        while not q.empty():
            u = q.get()
            for v in G[u]:
                if colors[v] == -1:
                    q.put(v)
                    colors[v] = (colors[u] + 1)%2 #if parent == 0: v = 1 i na odwrot
                elif colors[v] == colors[u]: #juz odwiedzone i widac ze u,v sa sasiednie a mają ten sam kolor
                    return False
        return True
    for start in range (len(G)):
        if colors[start] == -1:
            if not is_bipartite2(G,start):
                return False
    return True
    #to działa bo patrzymy zawsze na całe n(v), czyli gdy wystapi kolizja na pewno ją wykryjemy
            
graph = [[2,1,6],[0,3,2],[0,1,3],[2,1,4],[3,5],[4,6],[0,5]]
bipartite = [[]]
acyclic = [[1],[0,2],[1,3],[2]]
print("spojny:",is_connected([[3,4,6],[3,6],[3,6],[0,1,2,5],[0,7,8],[3],[0,1,2,7],[4,6],[4],[]]))
#print(is_acyclic(acyclic))
print(dwudzielnosc([[3,4,6],[3,6],[3,6],[0,1,2,5],[0,7,8],[3],[0,1,2,7],[4,6],[4],[]]))
bfs(graph,0)


