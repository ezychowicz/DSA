def topological_order(G):
    order = [None]*(len(G))
    visited = [False]*(len(G))
    idx = len(G) - 1
    def DFSvisit(i):
        nonlocal idx
        visited[i] = True
        for v in G[i]:
            if not visited[v]:
                visited[v] = True
                DFSvisit(v)
        order[idx] = i
        idx -= 1
    for u in range(len(G)):
        if not visited[u]:
            DFSvisit(u)
    return order