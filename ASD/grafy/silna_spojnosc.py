#17.04
def DFS1(G):
    visited = [False]*(len(G))
    order = [None]*(len(G))
    cnt = len(G) - 1
    def DFSVisit1(i):
        nonlocal cnt
        visited[i] = True
        for v in G[i]:
            if not visited[v]:
                DFSVisit1(v)
        order[cnt] = i       
        cnt -= 1
    for u in range (len(G)):
        if not visited[u]:
            DFSVisit1(u)
    return order
def SCC(G): #funkcja zwraca liste sąsiedztwa grafu SCC i tablice z zawartosciami poszczególnych skladowych
    visited = [-1]*(len(G))
    SCCs = []
    def translate(G): 
        G_T = [[] for _ in range (len(G))]
        for i in range (len(G)):
            for v in G[i]:
                G_T[v].append(i)
        return G_T
    comps = 0
    def DFSVisit(i,G):
        nonlocal comps,SCCs
        visited[i] = comps
        for v in G[i]:
            if visited[v] == -1:
                DFSVisit(v,G)
            elif visited[v] != comps: #odwiedzone, ale w poprzednim zyciu
                if comps not in SCCs[visited[v]]:
                    SCCs[visited[v]].append(comps) #na odwrot polaczenie wpisuje, bo tutaj pracujemy na transpozycji G
    
    order = DFS1(G)
    G_T = translate(G)

    for i in range (len(order)):
        if visited[order[i]] == -1:
            SCCs.append([])
            DFSVisit(order[i],G_T)
            comps += 1
            #elementy kazdej skladowej mozna odczytac w visited, wierzcholek i nalezy do visited[i] skladowej
    buckets = [[] for _ in range (len(SCCs))]
    for i in range (len(visited)):
        buckets[visited[i]].append(i)
    for i in range (len(buckets)):
        print(i,":",buckets[i])
    return SCCs

G = [[1],[2,4,5],[3],[7,2],[0,5],[6],[2,7,5],[]]
print(SCC(G))