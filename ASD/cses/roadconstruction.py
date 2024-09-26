class Node:
    def __init__(self,val):
        self.val = val
        self.parent = self
        self.rank = 0
        self.size = 1
    

def find(x):
    if x.parent != x:
        x.parent = find(x.parent)
    return x.parent

def union(x,y):
    x,y = find(x),find(y)
    if x == y:
        return
    if x.rank > y.rank:
        y.parent = x
        x.size += y.size
        return x.size
    elif x.rank < y.rank:
        x.parent = y
        y.size += x.size
        return y.size
    else:
        x.rank += 1
        y.parent = x
        x.size += y.size
        return x.size
def components(E,n):
    comps = n
    max_size = 1
    S = [Node(i) for i in range (n)]
    for u,v in E:
        if find(S[u - 1]) != find(S[v - 1]):
            comps -= 1
            max_size = max(max_size,union(S[u - 1],S[v - 1]))
        print(comps,max_size)

E = [(1,2),(1, 3),(4, 5)]
n = 5
components(E,n)