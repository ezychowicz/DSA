# '''In a party of N people, only one person is known to everyone. Such a person may be present at the party, 
# if yes, (s)he doesn’t know anyone at the party. We can only ask questions like “does A know B? “. 
# Find the stranger (celebrity) in the minimum number of questions.
# We can describe the problem input as an array of numbers/characters representing persons in the party. 
# We also have a hypothetical function HaveAcquaintance(A, B) which returns true if A knows B, and false otherwise. How can we solve the problem? '''  #zadanie ciekawostka
# #algocja
# #zwykly cykl eulera, mamy zapewnione ze nie bedziemy do miast wchodzic wielokrotnie bo mają tylko dwie krawedzie, wiec jedna wchodzimy drugą wychodzimy
# #zlaczyc oazy w superoazy
# def algocja(G,category): #G-macierz sasiedztwa
#     oasis = [-1]*(len(G))
#     cnt = 0
#     for i in range (len(G)):
#         if category[i] == "o":
#             if oasis[G[i]] == -1:
#                 oasis[G[i]] = cnt
#                 cnt += 1
#             for j in range (len(G[i])):
#                 if G[i][j] == 1 and category[G[i][j]] == "o":
#                     oasis[G[j]] = oasis[G[i]]
#     print(oasis)
#     super_oasis = [[] for _ in range (cnt)] #lacze oazy w jeden wierzcholek, wtedy nie ma polaczen miedzy oazami, tym samym kazda krawedz MUSI byc odwiedzona
#     for i in range (len(G)):
#         if oasis[i] != -1:
#             for j in range (len(G[i])):
#                 if category[G[i][j]] == "m":
#                     if G[i][j] not in super_oasis[oasis[i]]:
#                         super_oasis[oasis[i]].append(G[i][j])
#     for el in super_oasis:
#         if len(el)%2 == 1:
#             return False
#     #return True
#     v_edge = [[False for _ in range (len(G[i]))] for __ in range (len(G))]
#     v_super = [[False for _ in range (len(super_oasis[i]))] for i in range (len(super_oasis))]
#     circuit = []
#     def DFSVisit(i):
#         if oasis[i] != -1: #jesli weszlismy do oazy, przegladaj sasiadow superoazy w ktorej sie znajdujemy
#             for v in super_oasis[oasis[i]]:
#                 if not v_super[i][v]:
#                     v_super[i][v] = True
#                     DFSVisit(j)
#         else: #jesli zwykly wierzcholek to dodawaj jak w zwyklym cyklu eulera
#             for j in range (len(G[i])): 
#                 if G[i][j] == 1 and not v_edge[i][j]:
#                     v_edge[i][j] = True
#                     DFSVisit(j)
#         circuit.append(i)

# # Znalezc najkrotsze sciezki pomiedzy wszystkimi parami wierzcholkow
# #tabela kursow walut






# #domkniecie grafu
# # tablica dist otrzymywana w Floyd_warshall bedzie praktycznie tym samym co macierz sąsiedztwa grafu domknięcia
# #inf - brak krawedzi, 0 - krawedz

# def floyd_warshall(G):
#     N = len(G)
#     G_trans = [[float('inf') for _ in range (N)] for __ in range (N)]
#     for i in range (N):
#         G_trans[i][i] = 0
    
#     for i in range(N):
#         for j in range (N):
#             if G[i][j] != 0:
#                 G_trans[i][j] = 0
    
#     for k in range (N):
#         for x in range (N):
#             for y in range (N):
#                 if G_trans[x][k] != float('inf') and G_trans[k][y] != float('inf'):
#                     G_trans[x][y] = 0
    
#     print(*G,sep='\n')


# # Dana jest tabela kursów walut. Dla kazdych dwóch walut x oraz y wpis
# # K[x][y] oznacza ile trzeba zapłacic waluty x zeby otrzymac jednostke waluty y. Prosze zaproponowac algorytm,
# # który sprawdza czy istnieje taka waluta z, ze za jednostke z mozna uzyskac wiecej niz jednostke z
# # przez serie wymian walut.

# #chcemy znalezc taki cykl, w ktorym iloczyn kursów da liczbę >1. Wtedy ze złotówki otrzymamy np 1,21zł.
# #żeby to znalezc zamieniamy weight[i] na log(weight[i]). Teraz interesuje nas cykl o iloczynie > 1, czyli log > 0. Nie ma algorytmu na cykl o 
# #dodatniej sumie, ale jest na cykl o ujemnej (B.-F.). Możemy wszystkie wagi zamienić na odwrotne, wówczas wykryć ujemny cykl, który w rzeczywistości oznacza
# #cykl dodatni.

# from math import log 
# def convert(G):
#     for i in range (len(G)):
#         for j in range (len(G)):
#             G[i][j] = (G[i][j][0],-log(G[i][j][1],2))

# def bellman_ford(G):
#     convert(G)
#     N = len(G)
#     dist = [float('inf')]*(len(G))
#     for _ in range (N): #N razy
#         for i in range (N): #relaksujemy każdą krawedz
#             for v,w in G[i]:
#                 if dist[v] > dist[i] + w:
#                     dist[v] = dist[i] + w
    
#     for i in range (N):
#         for v in G[i]:
#             if dist[v] > dist[i] + w:
#                 return False
#     return True


# #zaplanować trasy wyścigów (cykle) tak aby przez każde miasto bitocji przechodził dokładnie jeden wyścig. każde miasto ma max 2 autostrady
# #wychodzace i wchodzace.
# ''' O(V*(V+E))
# 1. zliczac ilość cykli wychodzących z danych wierzchołkow.
# 2. jesli z jakiegos wierzcholka nie wychodzi cykl to False.
# 3. przejsc przez wszystkie wierzcholki jednocyklowe i odwiedzic cale cykle.
# 4. powtarzać tak dlugo az wszystkie wierzcholki bedą odwiedzone (kazdy wierzcholek ma juz jakis cykl jeden przypisany) albo zostaną same wierzcholki dwucyklowe to (nie istnieje taki graf)
# '''
# from queue import Queue
# def convert(count):
#     for i in range (len(count)):
#         count[i] = [count[i],i]

# def wyscigi(G):
import math
def distance(A,B):
    return (A[0] - B[0])**2 + (A[1] - B[1])**2
def create_graph(A): #stworz E
    E = []
    for i in range (len(A) - 1):
        for j in range (i + 1,len(A)):
            E.append((i, j, math.ceil((distance(A[i], A[j]))**(0.5))))
    return E

class Node:
    def __init__(self, val = 0):
        self.val = val
        self.parent = self
        self.rank = 0

def kruskal(E,i,N):
    def find(v):
        if v.parent != v:
            v.parent = find(v.parent)
        return v.parent
    def union(u,v):
        x,y = find(u), find(v)
        if x.rank < y.rank:
            x.parent = y
        elif x.rank > y.rank:
            y.parent = x
        else:
            x.rank += 1
            y.parent = x
    S = [Node() for _ in range (N)]
    res = -1
    cnt = 0
    for j in range (i,len(E)):
        u,v = E[j][0],E[j][1]
        if find(S[u]) != find(S[v]):
            cnt += 1
            union(S[u],S[v])
            res = E[j][2]
    return res if cnt == N - 1 else float('inf') #res to bedzie ostatnia dodana waga - czyli najwieksza waga

def highway(A):
    E = create_graph(A)
    E.sort(key = lambda x: x[2]) 
    mini = float('inf')
    N = len(A)
    print(E)
    for i in range (len(E) - N + 1):
        maxi = kruskal(E,i,N) #MST z krawedzi od i - tej do konca
        mini = min(mini,maxi - E[i][2])
    return mini
    
A = [(10,10),(15,25),(20,20),(30,40)]

print(highway(A))