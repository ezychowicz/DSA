#g.skierowany - warunek cyklu eulera: dla każdego v: inDegree(v) = outDegree(v)
#             - warunek scieżki eulera: istnieje x, y, że inDegree(x) = outDegree(x) - 1 i inDegree(y) = outDegree(y) + 1, wowczas da sie z x do y po wszystkich krawedziach
#g.nieskierowany - warunek cyklu eulera: dla kazdego v 2|d(v)
#                - warunek sciezki eulera: nieparzysty stopień ma albo 0 albo 2 wierzchołki
def List_to_matrix(G, weighted = False, zeros = True): # from list of lists G to matrix H
    if zeros:
        H = [[0 for __ in range(len(G))] for _ in range(len(G))]
    else:
        H = [[float('inf') for _ in range(len(G))] for __ in range(len(G))]
    if not weighted:
        for v, edges in enumerate(G):
            for u in edges:
                H[v][u] = 1
    else:
        for v, edges in enumerate(G):
            for u, weight in edges:
                H[v][u] = weight
    return H

#na macierzy sasiedztwa:
def get_eulers_circuit(G):
    def is_eulerian(G):
        for i in range (len(G)):
            cnt = 0
            for j in range (len(G)):
                if G[i][j]:
                    cnt += 1
            if cnt%2 == 1:
                return False
        return True
    if not is_eulerian(G):
        return False
    
    v_edge = [[False for _ in range (len(G))] for __ in range (len(G))]
    circuit = []
    def DFSVisit_edge(i):
        nonlocal circuit
        for v in range(len(G)):
            if G[i][v] and not v_edge[i][v]:
                v_edge[v][i],v_edge[i][v] = True,True
                DFSVisit_edge(v)
        circuit.append(i) #(preorder traversal?)tak naprawde to jest troche jak insertowanie dzieki rekurencji, słowem: dziala tak ze idzie sobie dfs az nie wejdzie do slepego zaulka tj. do startu cyklu. Potem rekurencja cofa tam gdzie pozostaly mozliwosci pojscia gdzies i appenduje tam te cykle pomniejsze
    DFSVisit_edge(0)
    return circuit

G = List_to_matrix([[1,7],[0,8,2,3],[1,3],[2,1,8,4],[3,5],[4,8,7,6],[5,7],[6,5,0,8],[7,5,3,1]])
#G = List_to_matrix([[1,2],[0,2,3,4],[0,1,3,4],[1,2],[1,2]])
print(get_eulers_circuit(G))


#na liscie sasiedztwa:
#1sp: analogiczny, wtedy zeby odznaczac krawedzie musimy przeszukiwac cale zbiory N(v), wiec O(V+E+E^2)
#2sp: zrobic se macierz krawedzi = praca na macierzy sasiedztwa  
#na skierowanym jest gdzeis zrobione

#dla skierowanych ( bez sprawdzenia )
def euler(G,R):
    def is_eulerian(G): # w macierzowej latwo policzyc przechodzac kolumnami i rzedami
        inDegree = [0]*(len(G)) 
        outDegree = [len(G[i]) for i in range (len(G))]
        for i in range (len(G)):
            for v in G[i]:
                inDegree[v] += 1
        return inDegree == outDegree
    if not is_eulerian(G):
        return False
    circuit = []
    progress = [0 for __ in range (len(G))]
    def DFSVisit(i):
        nonlocal circuit
        j = progress[i]
        while j < len(G[i]):
            progress[i] += 1
            DFSVisit(G[i][j])
            j = progress[i]
        circuit.append(i)
    
    DFSVisit(0)
    circuit.reverse()
    return circuit
