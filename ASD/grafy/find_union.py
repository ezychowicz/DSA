class Node:
    def __init__(self,val):
        self.val = val
        self.parent = val
        self.rank = 0
    
def find(v):
    if v.parent != v:
        v.parent = find(v.parent)
    return v.parent

def union(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x.rank > y.rank:
        y.parent = x
    elif x.rank < y.rank:
        x.parent = y
    else:
        x.parent = y
        y.rank += 1  
        


def MST(E,n):
    E.sort(key = lambda x: x[2])
    S = [Node() for _ in range (n)]

#zlozonosc zamortyzowana: srednia zlozonosc kazdej operacji

#najkrotszy cykl: usuwac kazda krawedz x,y i dijkstra z x do y: potem dodac wage wierzcholka z x do y  
#graf skierowany: floyd-warshall: probujemy kazda pare ktora jest polaczona krawedzia, i dodajemy wage krawedzi 