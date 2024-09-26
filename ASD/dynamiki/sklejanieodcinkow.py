#1) czy da sie uzyskać przedział [a,b] sklejając.
#f(i) = czy da sie osiagnac koncowke i-tego przedzialu zaczynajac w a

def sklejanie_odcinkow1(T,a,b):
    N = len(T)
    T.sort() #sortuj po poczatkach
    print(T)
    flag = False
    for s in range (len(T)):
        if T[s][0] == a:
            flag = True
            break
    if flag == False: #gdy nie ma przedzialu o poczatku w a
        return False
    first = s #indeks pierwszego przedzialu zaczynajacego sie na a
    F = [False]*(len(T))
    
    while T[s][0] == a: #wszystkie koncowki przedzialow o poczatku w a jestem w stanie osiagnac na pewno
        F[s] = True
        s += 1
    
    ends = []
    for i in range (first, N): #znajdz przedzialy docelowe
        if T[i][1] == b:
            ends.append(i)

    if not ends: #gdy nie ma przedzialu o koncu w b
        return False
    
    N = len(T)
    for i in range (s, ends[-1] + 1): #zaczynam patrzec od tych ktorych jeszcze nie zaznaczylem - tj. zaczynajacych sie na cos pozniejszego niz a
        for j in range (first, i): #nie patrze na wczesniejsze niz first, bo mają one poczatki mniejsze niż a, czyli takie sklejenie mi nic nie da. 
            if T[j][1] == T[i][0] and F[j]: #tzn istnieje przedzial zakonczony na tą samą liczbe na którą i-ty przedzial sie zaczyna i da sie dojsc do tego przedzialu
                F[i] = True
    for end in ends:
        if F[end]:
            return True
    return False

T = [[-1,4],[0,1],[2,4],[2,6],[3,5],[5,8],[6,8],[1,9],[8,9]]
a = 2
b = 9
#print(sklejanie_odcinkow1(T,a,b))
        

def sklejanie_odcinkow2(T,C,a,b): #C - tablica kosztów
    N = len(T)
    T.sort() 
    print(T)
    flag = False
    for s in range (len(T)):
        if T[s][0] == a:
            flag = True
            break
    if flag == False: 
        return -1
    first = s 
    F = [float('inf')]*(len(T))
    
    while T[s][0] == a: 
        F[s] = C[s] #najtanszy koszt dojscia do tego przedzialu to koszt wlasny (niekoniecznie jest to najtansza sciezka do konkretnej wartosci)
        s += 1
    
    ends = []
    for i in range (first, N): #znajdz przedzialy docelowe
        print(T[i])
        if T[i][1] == b:
            ends.append(i)

    if not ends: #gdy nie ma przedzialu o koncu w b
        return -1
    
    N = len(T)
    for i in range (s, ends[-1] + 1): 
        for j in range (first, i): 
            if T[j][1] == T[i][0]:
                F[i] = min(F[i], F[j] + C[i])
    mini = float('inf')
    for end in ends:  #interesuje nas najtansze przejscie do jednego z przedzialow koncowych bo np.[a,b]=[1,5]:[1,2]C=1, [1,5]C=100, [2,5]C=1: do 5 taniej dojsc "dluzszą" scieżką
        mini = min(F[end],mini)
    return mini if mini != float('inf') else -1
import random
T = [[-1, 4], [0, 1], [1, 2], [2, 4], [2, 6], [3, 5], [5, 8], [6, 8], [8, 9]]
C = [random.randint(1,10) for _ in range (len(T))]
#print(C)
#print(sklejanie_odcinkow2(T,C,a,b))



#troche LIS
#f(i,k) - maksymalna dlugosc taśmy kończącej się w i-tym przedziale zawierającej k odcinków
#odp: max(i)(f(i, K))
#f(i,k) = max(j < i, krawedz istnieje)(f(j, k-1)) + dist
def sklejanie_odcinkow3(T, K): #K = max. odcinków w taśmie
    T.sort()
    N = len(T)
    F = [[0 for _ in range (K + 1)] for __ in range (N)]
    for i in range (N): #gdy K=1 to po prostu dlugosci odcinkow to odp
        F[i][1] = T[i][1] - T[i][0]
    for i in range (1,N):
        for k in range (2,K + 1):
            for j in range (i):
                if T[j][1] == T[i][0]: #czy krawedz istnieje
                    F[i][k] = max(F[i][k], F[j][k - 1] + (T[i][1] - T[i][0]))
    maxi = -float('inf')
    for i in range (N):
        for k in range (K + 1):
            maxi = max(maxi, F[i][k])
    print(F)
    return maxi

T = [(0, 1), (1, 3), (2, 3), (3, 4), (5, 6), (6, 8), (8, 9)]
T = [(0, 1), (1, 3), (2, 3), (3, 4), (5, 6), (6, 8), (8, 9), (1, 7)]
print(sklejanie_odcinkow3(T,3))