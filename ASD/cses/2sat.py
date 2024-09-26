#jesli graf implikacji ma w jednym komponencie 2 sprzeczne formy atomowe to nie da sie dobrac odpowiednio wartosci logicznych
#https://cp-algorithms.com/graph/2SAT.html tu jest wyjasnione dobrze

def SCC(G,m):
    cnt = len(G) - 1
    visited = [False]*(len(G))
    order = [None]*(len(G))

    def trans(G):
        G_T = [[] for _ in range (len(G))]
        for i in range (len(G)):
            for v in G[i]:
                G_T[v].append(i)
        return G_T
    def DFSVisit(i):
        nonlocal cnt
        visited[i] = True
        for v in G[i]:
            if not visited[v]:
                DFSVisit(v)
        order[cnt] = i
        cnt -= 1

    def DFSVisit2(G,i,iter):
        visited[i] = iter
        if visited[-i - 1] == iter:
            return False
        for v in G[i]:
            if visited[v] == -1:
                if not DFSVisit2(G,v,iter):
                    return False
            elif visited[v] != iter:
                if iter not in SCCG[visited[v]]:
                    SCCG[visited[v]].append(iter)
        return True
    
    for i in range (len(G)):
        if not visited[i]:
            DFSVisit(i)

    G_T = trans(G)                              
    visited = [-1]*(len(G))
    SCCG = []
    for iter,v in enumerate(order):
        if visited[v] == -1:
            SCCG.append([])
            if not DFSVisit2(G,v,iter):
                return "IMPOSSIBLE"
    print("POSSIBLE")
    
    order = [None]*(len(SCCG))
    cnt = len(SCCG) - 1
    def DFSVisit(i):
        nonlocal cnt
        visited[i] = True
        for v in G[i]:
            if not visited[v]:
                DFSVisit(v)
        order[cnt] = i
        cnt -= 1
    buckets = [[] for _ in range (len(SCCG))]
    for i in range (len(visited)):
        buckets[visited[i]].append(i)
    log_val = [-1]*(m + 1) #-1 brak przypisanej wartosci logicznej, 0 fałsz, 1 prawda
    for i in range (len(order)):
        for v in buckets[i]:
            if log_val[v%m + 1] == -1: #tutaj jest poprzednik implikacji, chcemy zeby był fałszywy. gdyby był prawdziwy, a potem byśmy wykryli nie x to by implikacja była fałszywa. Jeśli z kolei dalej nie pojawia sie nie x to wywalone, mozemy przypisac cokolwiek wiec przypisujemy falsz
                if v >= m: #zaprzeczenie ma byc falszywe
                    log_val[v%m + 1] = 1 #w(x) = 1
                else:
                    log_val[v%m + 1] = 0 #w(x) = 0
    return log_val

#TU JEST Z TYMI M POPIEPRZONE, BEZ SENSU