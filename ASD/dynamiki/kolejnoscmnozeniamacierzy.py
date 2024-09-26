#f(i,end) - krotka:k[1]=wymiary,k[0]=minimalny koszt pomnozenia macierzy w taki sposob że (A1*A2*A3*A4*...*Ai)(Ai+1*Ak+2*...*Aend) (macierze z róznych nawiasów się już nie mieszają)
#f(i,end) = min(i<j<end)(f(i,j)[0] (koszt lewej) + f(j + 1,end)[0] (koszt prawej) + cost(f(i,j)[1],f(j + 1,end)[1] (koszt wymnozenia lewej i prawej))),wymiary #taka podzialka ze koszt wymnozenia najmniejszy,zapisz wymiary bo potrzebne do wyliczania kosztów 
#base case: if end - i + 1 == 2: f(i,end) = ni*ki*ki+1,ni x ki+1 gdzie ni,ki to wymiary macierzy
#base case: if end - i + 1 == 1: f(i,end) = 0, ni x ki

def matrix_product_cost(T): #T = [(n0,k0),(k0,k1),(k1,k2),...,(kn-1,kn)]
    def cost(A,B):
        return A[0]*A[1]*B[1]
    N = len(T)
    F = [[(float('inf'),None) for _ in range (N)] for __ in range (N)]
    for i in range (len(T)):
        F[i][i] = (0,T[i])

    def f(i,end):
        if F[i][end][0] != float('inf'):
            return F[i][end]
        if end - i + 1 == 2:
            F[i][end] = (cost(T[i],T[end]),(T[i][0],T[end][1]))
            return F[i][end]
        mini = float('inf')
        for j in range (i,end):
            check = f(i,j)[0] + f(j + 1,end)[0] + cost(f(i,j)[1],f(j + 1,end)[1])
            if check < mini:
                mini = check 
                save = j
        print(mini,i,save,end)
        F[i][end] = (mini,(T[i][0],T[end][1]))
        return F[i][end]
    return f(0,len(T) - 1)


T = [(6,9),(9,7),(7,5),(5,4),(4,1)]
print(matrix_product_cost(T))


