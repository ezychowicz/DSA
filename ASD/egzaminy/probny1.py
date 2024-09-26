def find(x):
    if x.parent != x:
        x.parent = find(x.parent)
    return x.parent

def union(x,y):
    x,y = find(x), find(y)
    if x == y:
        return
    if x.rank > y.rank:
        y.parent = x
    elif x.rank < y.rank:
        x.parent = y
    else:
        x.rank += 1
        y.parent = x 
def four_edges(E,low_bound): #O(E)
    for i in range (low_bound,len(E)):

def turysta(G,D,L):
    G.sort(key = lambda x: x[2])
    for low_bound in range (len(G)):
        res =  four_edges(G,low_bound)
        if res != -1:
            return res
         