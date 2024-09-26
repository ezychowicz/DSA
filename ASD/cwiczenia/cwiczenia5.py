from math import inf

def Matrix_to_list(G): # from matrix G to list of lists H
    H = [[] for _ in range(len(G))]
    for i in range(len(G)):
        for j in range(len(G)):
            if G[i][j] != inf:
                H[i].append((j, G[i][j]))
    return H

def List_to_matrix(G, weighted = False, zeros = True): # from list of lists G to matrix H
    if zeros:
        H = [[0 for __ in range(len(G))] for _ in range(len(G))]
    else:
        H = [[inf for _ in range(len(G))] for __ in range(len(G))]
    if not weighted:
        for v, edges in enumerate(G):
            for u in edges:
                H[v][u] = 1
    else:
        for v, edges in enumerate(G):
            for u, weight in edges:
                H[v][u] = weight
    

    return H
#usuwanie od konca

def pause(G):
    visited = [False]*(len(G))
    time = 0
    v_sorted = [None]*(len(G))
    cnt = 0
    def DFSVisit(i):
        nonlocal cnt
        visited[i] = True
        for v in G[i]:
            if not visited[v]:
                DFSVisit(v)
        v_sorted[cnt] = i
        cnt += 1
    start = 0
    DFSVisit(start)
    return v_sorted

#print(pause([[6],[6,2],[1,6,3],[4,2],[3,5],[4,6],[5,7,0,1,2],[6]]))
        

#wykrywanie C4
def cycle_4(G): #brute force, wszystkie sciezki o dlugosci 4 sprawdzane dla kazdego wierzcholka O(V*V)?
    visited = [False]*(len(G))
    def check(start,i,cnt):
        visited[i] = True
        if cnt == 3:
            for v in G[i]:
                if start == v:
                    return True
            return False
        for v in G[i]:
            if not visited[v]:
                if check(start,v,cnt+1):
                    return True
        return False
    for i in range (len(G)):
        visited = [False]*(len(G))
        if check(i,i,0):
            return True
    return False
#better?
'''
Dodaje krawedzie miedzy wszystkimi dwuelementowymi zbiorami krawedzi ze zbioru N(v) dla wszystkich v.
Gdy dwa razy zostanie dodana ta sama krawędź, oznacza to że istnieje cykl C4: Mamy dwa różne wierzchołki, które mają
dwóch wspólnych sąsiadów. Niezależnie od tego czy ci sąsiedzi są połączeni czy nie, mamy 4 wierzchołki, dwa z nich mają dwóch wspólnych sąsiadów - musi być tam 
podgraf C4. https://mathoverflow.net/questions/67960/cycle-of-length-4-in-an-undirected-graph  O(V^3)
'''
#tutaj szukamy dwa wierzcholki o co najmniej 2 wspolnych krawedziach
# def cycle_4(G): 
#     V = len(G)
#     T = [[0 for _ in range (V)] for _ in range (V)]
#     def all_pairs(i):
#         nonlocal T
#         for j in range (len(G[i])-1):
#             for k in range (j+1,len(G[i])):
#                 if T[G[i][j]][G[i][k]] == 2:
#                     #print(G[i][j],G[i][k])
#                     return True
#                 else:
#                     T[G[i][j]][G[i][k]] = 2
#                     T[G[i][k]][G[i][j]] = 2
#         return False

#     # for i in range (len(G)):
#     #     for j in range (len(G[i])):
#     #         T[i][G[i][j]] = 1
#     #         T[G[i][j]][i] = 1

#     for i in range (V):
#         if all_pairs(i):
#             return True
#     return False 


#print(cycle_4([[3],[2],[1,4,3],[0,2,4],[3,2]]))
# print(cycle_4([[6],[6,2],[1,6,3],[4,2],[3,5,6],[4,6],[5,7,0,1,2,4],[6]]))
#z cwiczen
def cycle_4(G): #m.sasiedztwa
    N = len(G)
    for i in range (N-1):
        for j in range (i+1,N):
            cnt = 0
            for k in range (N):
                if k != i and k != j:
                    if G[i][k] == G[j][k] == 1:
                        cnt += 1
                if cnt == 2:
                    return True
    return False
G = List_to_matrix([[3],[2],[1,4,3],[0,2,4],[3,2]])
#print(cycle_4(G))
#print(cycle_4([[6],[6,2],[1,6,3],[4,2],[3,5,6],[4,6],[5,7,0,1,2,4],[6]]))
#uniwersalne ujście - ujście definiujemy jako wierzchołek v taki ze dla wszystkich u z grafu u->v, a stopien wychodzących v wynosi 0

def funnel(G):
    def is_possible(G):
        cnt = 0
        for i in range (len(G)):
            for j in range (len(G)):
                if G[i][j] == 1:
                    break
                if j == len(G) - 1:
                    cnt += 1
                    if cnt > 2:
                        return -1
                    else:
                        save = i
        if cnt == 0:
            return -1
        return save
    candidate = is_possible(G)
    if candidate == -1:
        return False
    for j in range (len(G)):
        if G[j][candidate] == 0:
            return False
    return True


#CWICZENIA

#czy spojny

#skladowe spojne - ile

def skladowe(A):
    visited = [False]*(len(A))
    cnt = 0
    def DFSvisit(i):
        visited[i] = True
        for j in range (len(A)):
            if A[i][j] == 1 and not visited[j]:
                DFSvisit(j)   
    for v in range (len(A)):
        if not visited[v]:
            DFSvisit(v)
            cnt += 1 
    return cnt

#znalezc sciezke do danego wierzcholka BFS+parent
import queue
def bfs(G,start,visited,parent):
    q = queue.Queue()
    visited[start] = True
    q.put(start)
    while not q.empty():  
        u = q.get()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                q.put(v)
                parent[v] = u

def restore_path(G,dest):
    visited = [False]*(len(G))
    parent = [None]*(len(G))
    for i in range (len(G)):
        if not visited[i]:
            bfs(G,i,visited,parent)
    i = dest
    ans = []
    while i != None:
        ans.append(i)
        i = parent[i]
    ans.reverse()
    return ans

#print(restore_path([[6],[6,2],[1,6,3],[4,2],[3,5],[4,6],[5,7,0,1,2],[6]],3))


#ujscie na macierzy sasiedztwa
#sposob z sortowaniem topologicznym O(V + V + V)
def topological_sort(G):
    color = [-1]*(len(G))
    t_sorted = [None]*(len(G))
    cnt = 0
    def DFSVisit(i):
        nonlocal cnt
        color[i] = 0
        for j in range (len(G)):
            if G[i][j] == 1: 
                if color[j] == -1:
                    return DFSVisit(j)
                elif color[j] == 0:
                    return False #czy DAG
        t_sorted[-1-cnt] = i
        color[i] = 1
        cnt += 1
        return True
    for i in range (len(G)):
        if color[i] == -1:
            if not DFSVisit(i):
                return [False]
    return t_sorted
def check(G,t_sorted):
    if t_sorted[0] == False:
        return False
    candidate = t_sorted[-1]
    N = len(G)
    for i in range (len(t_sorted)-1):    
        if G[t_sorted[i]][candidate] == 0:
            return False
    return t_sorted[-1]
G = List_to_matrix([[],[0],[0,1],[0],[0,1],[0,4],[0,3,2],[0,3]]) #musi byc DAG, jesli ma cykl to nie ma ujscia
# print(*G,sep='\n')
# print("\n")
#print(check(G,topological_sort(G)))
#print(skladowe(G))

#sposob z zajęc: mądre przechodzenie po macierzy
def ujscie(G):
    i,j = 0,0
    N = len(G)
    while i < N and j < N:
        if G[i][j] == 1 or (G[i][j] == 0 and i == j):
            i += 1
        else:
            j += 1
            i += 1
        if j == N:
            return -1
        if i == N:
            break
    #j = candidate
    for i in range(len(G)):
        if G[j][i] == 1:
            return False
        if G[i][j] == 0 and i != j:
            return False
    return j
     
#print(ujscie(G))


#malejace krawedzie

#krawedzie 0/1  O(E^V?)
def krawedzie01(G,s,t):
    path = [None]*(len(G))
    def DFSVisit(i,end,cnt):
        mini = float('inf')
        if i == end:
            return 0
        for v in G[i]:
            path[cnt] = v[0]
            price = v[1] + DFSVisit(v[0],end,cnt+1)  #w sumie to chyba nie dziala bo jednak visited by sie przydalo (visited takie rekurencyjne,lokalne nie grafowe)
            mini = min(price,mini)
            path[cnt] = None
        return mini
    path[0] = s
    print(DFSVisit(s,t,1))
    return path
G = [[(1,0),(2,1)],[(3,0)],[(5,1)],[(2,1),(4,0)],[(2,0)],[]] #(v,val)
#print(krawedzie01(G,0,5))

#krawedzie 0/1 ale O(V+E)
def bfs_double_queues(G,s,t): #dwie kolejki, jedna na wierzcholki do ktorych wchodzi krawedz 0, druga dla 1. Jesli sie da bierzemy zera, gdy sie skoncza probujemy jedynki. Koszt zliczamy tylko przy jedynkach, i to przy faktycznym ich uzyciu, a nie dodaniu do kolejki
    visited = [False]*(len(G))
    q0,q1 = queue.Queue(),queue.Queue()
    q0.put(s)
    #visited[s] = True
    cnt = 0
    ans = []
    mini = [float('inf')]*(len(G))
    parent = [None]*(len(G))
    while True:
        if not q0.empty():
            u = q0.get()
        else:
            u = q1.get()
            print(u,visited[u])
            if not visited[u]: 
                cnt += 1
        visited[u] = True  #visited odznaczane jak w dfsie bardziej, dopiero po wejściu do danego wierzchołka
        if u == t:
            return cnt,parent
        for v in G[u]:
            if not visited[v[0]]:
                parent[v[0]] = u
                if v[1] == 1:
                    q1.put(v[0])
                else:
                    q0.put(v[0])
G = [[(1,0),(2,1)],[(3,0)],[(5,1)],[(2,1),(4,0)],[(2,0)],[]] 
print(bfs_double_queues(G,0,5))

#kosztowna szachownica
def szachownica(A,start):
    n = len(A)
    #dist = [0]*(n**2)
    q = queue.Queue()
    visited = [[False for _ in range (n)] for _ in range (n)]
    moves = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    q.put((start,A[start[0]][start[1]],0))
    while not q.empty(): #q = [((i,j),cnt,dist)]*?
        u = q.get()
        if u[1] >= 1:
            q.put(u[0],u[1]-1,u[2] + 1) #adding part
        else:
            visited[u[0]][u[1]] = True #dopiero tutaj zaznaczam bo tutaj dopiero dochodzimy rzeczywiscie do tego wierzcholka (visited mam tylko dla prawdziwych wierzcholkow a nie dla pachołów)
            if u[0][0] == n - 1 and u[0][1] == n - 1:
                return u[2]
            for move in moves: #adding part
                new_i,new_j = u[0][0] + move[0],u[0][1] + move[1]
                if new_i > n - 1 or new_j > n - 1 or visited[new_i][new_j]:
                    continue
                q.put(((new_i,new_j),A[new_i][new_j],u[2] + 1))


#z min_heapem:




            




