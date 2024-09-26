#f(k,i) - ilosc sposobow na uzyskanie k uzywając liczb do i-tego indeksu włącznie (ale nie koniecznie z itym idxem)
#odp: f(n,N - 1)
#f(k,i) = f(k, i - 1) (nie uzywam i-tego indeksu) + f(k - A[i], i)  (uzywam i-ty indeks, wtedy odsylam 
#do i tego indeksu bo moge go uzyc wielokrotnie)
#O(n*len(A))
def coin_comb(n,A): 
    F = [[0 for i in range (n + 1)] for i in range (len(A))]
    A.sort()
    x = A[0]
    F[0][x] = 1 #wypelnienie i=0
    while x <= n:
        F[0][x] = 1
        x += A[0]
    for i in range (len(A)):
        F[i][0] = 1
    for i in range (1, len(A)):
        for k in range (n + 1):
            print(F)
            if k < A[i]:
                F[i][k] = F[i - 1][k]
                continue
            F[i][k] = F[i - 1][k] + F[i][k - A[i]]
    return F[-1][-1]


print(coin_comb(9,[2,3,5]))

#2sp: rozsadniej iterowac po monetach: kazda moneta odwiedzana tylko raz
#f(i) - ilosc ciagow niemalejących do i-tego indeksu
#odp: f(N - 1)
#f(i) = f(i)