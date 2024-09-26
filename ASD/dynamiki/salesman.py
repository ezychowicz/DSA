#TSP bitoniczny na R^2
#bitonic tj. najpierw rosnący potem malejący lub na odwrot
#TSP bitoniczny: najpierw idziemy ciagle w prawo potem ciagle w lewo

def TSP(T): #T - wspolrzedne punktow
    def d(A,B):
        return ((A[0] - B[0])**2 + (A[1] - B[1])**2)**(0.5)
    T.sort(key = lambda x: x[0]) #sortuj po odciętych
    F = [[float('inf') for _ in range (len(T))] for __ in range (len(T))] 
    def f(i,j):
        if F[i][j] != float('inf'):
            return F[i][j]
        if i == j - 1:
            for k in range (i):
                F[i][j] = min(F[i][j], f(k, j - 1) + d(T[k],T[j]))
        else:
            F[i][j] = f(i, j - 1) + d(T[j - 1],T[j])
        return F[i][j]
