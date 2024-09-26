def LIS(T):
    def restore_sol(P,k):
        i = k
        sol = []
        while i != None:
            sol.append(T[i])
            i = P[i]
        sol.reverse()
        return sol
            
    F = [1]*len(T)
    P = [None]*(len(T))
    for i in range (1,len(T)):
        for j in range (i):
            if T[j] < T[i] and F[i] < F[j] + 1:
                P[i] = j
                F[i] = F[j] + 1
    k = F.index(max(F))
    return restore_sol(P,k)

print(LIS([2,2,4,1,2,1,2,7,8,5,11,7]))
                
    

def LIS_nlogn(T):
    #f(i) - najmniejsze zakonczenie ciągu dlugosci i
    #odp: |Df| (len(f))
    #f(i) = min(aktualne zakonczenie, T[i]) if T[i] > f(i - 1) lub gdy T[i] > f(N - 1): f(N) = T[i] (zwieksz dziedzine)  
    #len(F) to aktualnie największa długość LIS - 1: jeśli jesteśmy w stanie przdłużyć to dajemy append.
    def bin_search(F,key):
        left = 0
        right = len(F) - 1
        while left < right:
            mid = (left + right + 1)//2
            if F[mid] < key:
                left = mid
            else:
                right = mid - 1
        return left + 1 #F[left] można predłużyć czyli F[left + 1] jest nowe

    N = len(T)
    F = [-float('inf')] 
    
    for i in range (N):
        idx = bin_search(F,T[i]) 
        if idx == len(F):
            print("dla indeksu",idx - 1,"przedluzeniem jest",T[i])
            F.append(T[i])
        else:
            if F[idx] > T[i]:
                print(idx,T[i])
            F[idx] = min(F[idx], T[i]) #czy zmniejsza zakonczenie ciągu idx + 1
    return len(F) - 1, F

print(LIS_nlogn([2,2,4,1,2,1,2,7,8,5,11,7]))
                