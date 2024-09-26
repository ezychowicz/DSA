def adjlist_to_edges(G):
    E = []
    for i in range (len(G)):
        for v in G[i]:
            E.append((i,v))
    return E
def edges_to_adjlist(E):
    def find_max(E):
        maxi = -1
        for u,v in E:
            maxi = max(maxi,u,v)
        return maxi
    size = find_max(E) + 1
    G = [[] for _ in range (size)]  
    for u,v in E: #jesli skierowany lub gdy zawiera zarowno (u,v) jak i (v,u)
        G[u].append(v)

