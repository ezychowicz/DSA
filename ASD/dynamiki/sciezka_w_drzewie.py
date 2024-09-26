#najbardziej wartosciowa sciezka w drzewie gdzie kazdy wierzcholek ma wartosc, dopuszczalnie ujemna
#f(v) - najbardziej wartociowa sciezka zaczynajaca sie w v
#odp: f(korzen)
#f(u) = max(v in children[u])(f(v)) + val.u

#prawdopodobnie latwiej by bylo base case'y zrobić gdyby: 
#f(v) - najbardziej wartościowa sciezka koncząca sie w v z T 
#odp: max(v)(f(v))
#base case: f(T) = T.val
#f(u) = max(v in parent[u])(f(v)) + u.val
class Node():
    def __init__(self,val, children = []):
        self.val = val
        # self.parent = []
        self.children = children
        self.idx = 0
def drzewko(T): #T - korzen
    cnt = 0
    leaves = []
    def DFSVisit(i): #zlicza wierzchołki i zapisuje liście
        nonlocal cnt
        for v in i.children:
            DFSVisit(v)
        i.idx = cnt
        cnt += 1
        if i.children == []:
            leaves.append(i) #zapisz liście

    DFSVisit(T)
    F = [-float('inf') for i in range (cnt)]

    for leaf in leaves: #dla liści najdluzsza sciezka zaczynająca sie w nich to po prostu ich wartość
        F[leaf.idx] = leaf.val
    
    def f(u):
        if F[u.idx] != -float('inf'):
            return F[u.idx]
        maxi = -float('inf')
        for v in u.children:
            maxi = max(maxi, f(v))
        F[u.idx] = maxi + u.val
        return F[u.idx]
    return f(T)



root = Node(20, [
    Node(5, [
        Node(30), 
        Node(-20)
    ]), 
    Node(-20, [
        Node(1, [
            Node(30), 
            Node(22),
            Node(-15)
        ]), 
    ]), 
    Node(15),
    Node(-10, [
        Node(18),
        Node(23),
        Node(-20, [
            Node(100)
        ]),
        Node(-15)
    ])
])

print( drzewko(root) )