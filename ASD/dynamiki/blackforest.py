#czy nie przejdzie: f(i) = max(j<i-1){f(j) + c[i]} f(i)-max dochód jeśli BIERZEMY (i konczymy na nim)i-te drzewo. odp:max(f(i))
#optymalnie: f(i)=max(f(i-1),f(i-2)+c[i]) f-max do i wierzcholka
def blackforest(T):
    N = len(T)
    F = [[0,0] for _ in range (N)] #F[i][0] = nie bierz i-tego drzewa 
    P = [[None,None] for _ in range (N)]
    F[0][0], F[0][1] = 0, T[0]
    for i in range (1,N):
        F[i][0] = max(F[i - 1][0], F[i - 1][1])
        if F[i - 1][0] > F[i - 1][1]: #restore path
            P[i][0] = 0
        else:
            P[i][0] = 1 
        F[i][1] = F[i - 1][0] + T[i]
        P[i][1] = 0
    
    #restore path
    end = F[N - 1].index(max(F[N - 1]))
    next = end
    for i in range (N - 1, - 1, -1):
        if next == 1:
            print(T[i],end = ' ')
        next = P[i][next]  
    print('')  
    return max(F[N - 1])
    
print(blackforest([1,4,3,6,8,4,9]))