#z.2
import random,time
T=[(random.randint(0,999),random.randint(0,999)) for _ in range (random.randint(3,500))]
def zad_2(T):
    Nt=len(T)
    poz=[0]*1000
    pion=[0]*1000
    skos_g=[0]*1999
    skos_d=[0]*1999
    for i in range (Nt):
        poz[T[i][0]]+=1
        pion[T[i][1]]+=1
        skos_g[T[i][0]+T[i][1]]+=1
        skos_d[T[i][0]-T[i][1]]+=1
    for i in range (Nt):
        if poz[T[i][0]]==1 and pion[T[i][1]]==1 and skos_g[T[i][0]+T[i][1]]==1 and skos_d[T[i][0]-T[i][1]]==1:
            return False
    return True
start=time.time()
print(zad_2(T))
end=time.time()
print(end-start)
def sposob_gorszy(T):
    Nt=len(T)
    bool_tab=[False for _ in range (Nt)]
    for i in range (Nt-1):
        for j in range (i+1,Nt):
            if T[i][0]==T[j][0] or T[i][1]==T[j][1] or T[i][0]+T[i][1]==T[j][0]+T[j][1] or T[i][0]-T[i][1]==T[j][0]-T[j][1]:
                bool_tab[i]=bool_tab[j]=True
    return True if False not in bool_tab else False
start=time.time()
print(sposob_gorszy(T))
end=time.time()
print(end-start)