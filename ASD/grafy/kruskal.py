class Node():
    def __init__(self, value = 0):
        self.val = value
        self.parent = self
        self.rank = 0

def find(v):
    if v.parent != v:
        v.parent = find(v.parent)
    return v.parent

#albo tak:
# if v.parent == v:
#     return v.parent
# v.parent = find(v.parent)
# return v.parent bo musi cos zwracac przeciez gdy jest rozne
def union(u,v):
    x = find(u)
    y = find(v)
    if x == y:
        return 
    if x.rank > y.rank:
        y.parent = x
    elif x.rank < y.rank:
        x.parent = y
    else:
        y.rank += 1
        x.parent = y

def MST(E, n): #n - ilość wierzchołków
    S = [Node(i) for i in range (n)]
    res = []
    E.sort(key = lambda x: x[2])
    for u,v,w in E:
        if find(S[u]) != find(S[v]):
            union(S[u],S[v])
            res.append((u,v))
    return res

G1 = [
    [(1, 2), (3, 6)],
    [(0, 2), (2, 3), (3, 8), (4, 5)],
    [(1, 3), (4, 7)],
    [(0, 6), (1, 8), (4, 9)],
    [(1, 5), (2, 7), (3, 9)]
]

G2 = [
    [(1, 1), (2, 4)],
    [(0, 1), (2, 2), (3, 6)],
    [(0, 4), (1, 2), (3, 3)],
    [(1, 6), (2, 3)]
]

G3 = [
    [(1, 3), (2, 1)],
    [(0, 3), (2, 7), (3, 5), (4, 1)],
    [(0, 1), (1, 7), (4, 3)],
    [(1, 5), (4, 6), (5, 2)],
    [(1, 1), (2, 3), (3, 6), (5, 4)],
    [(3, 2), (4, 4)]
]

def adjlist_to_edges(G):
    E = []
    for i in range (len(G)):
        for v,w in G[i]:
            E.append((i,v,w))
    return E

print(MST(adjlist_to_edges(G3),len(G3)))