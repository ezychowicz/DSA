#double knapsack, no skipping
#f(i,S1,S2) - maksymalna liczba samochodow ktore mozemy zapakowac na pasy o dlugosciach S1, S2 do i-tego wyrazu
def knapsack(A,L):
    A.reverse() #żeby brał od przodu nie od tyłu, możnaby pewnie zrobić całość na odwrót ale za trudne to XD
    N = len(A)
    F = [[[0 for _ in range (L + 1)] for __ in range (L + 1)] for ___ in range (N)]
    #base case: i = 0
    for s1 in range (A[0],L + 1):
        for s2 in range (L + 1):
            F[0][s1][s2] = 1
            F[0][s2][s1] = 1 
    for i in range (1, N):
        
        for s1 in range (L + 1):
            for s2 in range (L + 1):
                if s1 - A[i] >= 0:
                    print(i,s1,A[i])
                    F[i][s1][s2] = F[i - 1][s1 - A[i]][s2] + 1
                if s2 - A[i] >= 0 and F[i - 1][s1][s2 - A[i]] + 1 > F[i][s1][s2]:
                    F[i][s1][s2] = F[i - 1][s1][s2 - A[i]] + 1
        print(*F,sep="\n")
    return F[N - 1][L][L]

A = [9,1,1,1,1,1,1,19]
L = 8
print(knapsack(A,L))
