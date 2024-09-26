def push(T,i,key):
    if T[i] == None:
        T[i] = key
        return    
    N = len(T)
    while i < N:
        T[i],key = key,T[i]
        i += 1

def push_back(T,i):
    N = len(T)
    while i <  N-1 and T[i] != None:
        T[i] = T[i+1]
        i += 1
    T[i] = None    

def insert(T,key):
    N = len(T)
    i = 0
    if T[i] == None:
        T[i] = key
        return
    while i < N and T[i] != None and T[i] < key:
        i += 1
    push(T,i,key)

def delete(T,key):
    N = len(T)
    i = 0
    while i < N and T[i] < key:
        i += 1
    push_back(T,i)

