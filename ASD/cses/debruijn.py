def convert(num,n): #liczba,ile cyfr ma byc w postaci binarnej
    res = [0]*(n)
    cnt = n - 1
    while num != 0:
        res[cnt] = num%2
        num //= 2
        cnt -= 1
    return res 
def convert_back(s):
    i = 0
    res = 0
    for el in s[::-1]:
        res += el*2**(i)
        i += 1
    return res

def create_graph(n): #tworzy graf n - 1 wymiarowy, dozwolone pętle, (podobny do hiperkostki), gdzie krawędź istnieje wtw. ostatnie litery jednego stringa to pierwsze litery drugiego (np. 001 -> 010, 011)
    n -= 1
    G = [[] for _ in range (2**(n))]
    for i in range (2**(n)):
        res = convert(i,n)
        new1,new2 = res[1:],res[1:]
        new1.append(0)
        new2.append(1)
        to_append1, to_append2 = convert_back(new1),convert_back(new2)
        # if to_append1 == i:
        #     G[i].insert(0,to_append1)
        #     G[i].append(to_append2)
        #     continue
        # if to_append2 == i:
        #     G[i].insert(0,to_append2)
        #     G[i].append(to_append1)
        #     continue
        G[i].append(to_append1)
        G[i].append(to_append2)
        
    return G


#wszystko ma na pewno dwie krawedzie wiec nie trzeba sprawdzac

def euler(G,n):
    n -= 1
    progress = [0]*(len(G))
    circuit = []
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
    res = [0]*n #zaczynamy od zera
    #res = [] 
    for i in range (1,len(circuit)):
        res.append(circuit[i]%2) #dodaj ostatnią cyfre binarki
    return res


n = 3
G = create_graph(n) #lol pewnie dalo sie tak od razu XD
print(euler(G,n),len(euler(G,n)))