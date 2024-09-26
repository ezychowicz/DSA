def DFS(G):
    visited = [False]*(len(G))
    time = 0
    def DFSvisit(i):
        nonlocal visited,G,time
        visited[i] = True
        time += 1
        for v in G[i]:
            if not visited[v]:
                visited[v] = True
                DFSvisit(v)
        time += 1 #czas przetworzenia wierzchołka (opcjonalne)
    cnt = 0
    for u in range(len(G)):
        if not visited[u]:
            DFSvisit(u)
            cnt += 1
    if cnt == 1:
        print("spojny")

def is_acyclic(G):
    visited = [False]*(len(G))
    parent = [None]*(len(G))
    def DFSvisit(i):
        nonlocal G,visited
        visited[i] = True
        is_ok = True
        for v in G[i]:
            if not visited[v]:
                visited[v] = True
                parent[v] = i
                is_ok = DFSvisit(v)
                if not is_ok:
                    return is_ok 
            else:
                if parent[i] != v:
                    return False
        return is_ok
    for u in range(len(G)):
        if not visited[u]:
            if not DFSvisit(u):
                return False
    return True

def is_bipartite(G):
    visited = [False]*(len(G))
    parent = [None]*(len(G))
    flags = [False]*(len(G)) #wystarczą dwie wartości bo analizujemy tylko odwiedzone wierzchołki (w rozwiazaniu z kolorwaniem w bfs analizowalismy wszystkie, choć latwo byloby sprowadzic to do tego samego)
    def DFSvisit(i):
        nonlocal G,visited,flags
        visited[i] = True
        is_ok = True
        for v in G[i]:
            if not visited[v]:
                visited[v] = True
                parent[v] = i
                flags[v] = not flags[i]
                is_ok = DFSvisit(v)   #zeby nie zwracal True jak tylko dla jednego wierzcholka bedzie sie zgadzac (jak w szachach gdy trzeba sprawdzic caly rzad czasem)
                if not is_ok:
                    return False
            else:
                if flags[i] == flags[v]:
                    print(i,v)
                    return False
        return is_ok
    for u in range(len(G)):
        if not visited[u]:
            flags[u] = True
            if not DFSvisit(u): #jesli ktorykolwiek z podgrafow spojnych nie jest dwudzielny to graf nie jest dwudzielny, jesli natomiast wszystkie są to caly graf jest dwudzielny
                return False
    return True

print(is_bipartite([[3,4,6],[3,6],[3,6],[0,1,2,5],[0,7,8],[3],[0,1,2,7],[4,6],[4],[]]))

def dfs_stack(G):
    visited = [False]*(len(G))
    time = 0
    def visit_below(i):
        nonlocal time
        stack = [i]
        while stack:
            #print(stack)
            u = stack.pop()
            if not visited[u]:
                print(u,end = ' ')
                visited[u] = True
                for v in G[u]:
                    if not visited[v]:
                        stack.append(v)            
    for start in range (len(G)):
        if not visited[start]:
            visit_below(start)

print(dfs_stack([[1,2,4],[0,2],[1,0,4,5],[4],[3,2,0],[2]]))



            