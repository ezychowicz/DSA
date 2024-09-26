#f(i,j) - LCS do i i j włącznie (nie muszą konczyc sie na i, j)
#odp: f(N - 1, N - 1)
#f(i,j) = max(f(i - 1,j),f(i,j - 1)) + 1 if T[i] == T[j]  #TO ZLE JEST f(i-1,j-1)+1 powinno byc po prostu
#else: max(f(i - 1,j),f(i,j - 1))
def LCS(T1,T2):
    N1 = len(T1)
    N2 = len(T2)
    F = [[0 for _ in range (len(T2))] for __ in range (len(T1))]
    flag = False
    # for i in range (N1): #base case'y: F[i][0] = 1 gdy T1[i] = T2[0] lub dla wczesniejszego i zaszla ta zaleznosc
    #     if T2[0] == T1[i]:
    #         F[i][0] = 1
    #         flag = True
    #     if flag:
    #         F[i][0] = 1
    # flag = False
    # for j in range (N2):
    #     if T1[0] == T2[j]:
    #         F[0][j] = 1 
    #         flag = True
    #     if flag:
    #         F[0][j] = 1
    if T1[0] == T2[0]:
        F[0][0] = 1 
    for i in range (1,N1):
        for j in range (1,N2):
            if T1[i] == T2[j]:
                F[i][j] = F[i - 1][j - 1] + 1
            else:
                F[i][j] = max(F[i - 1][j],F[i][j - 1])
    print(F)
    return F[N1 - 1][N2 - 1]

print(LCS(T1 = [7,5,4,2,1,8,2,3], T2 = [1,5,7,2,8,4,1,8]))

#zastosowanie do LIS: mozna ten algorytm uruchomic dla T i T.sorted() i wtedy otrzymujemy LIS
