#f(i) - nadluzsza wieza zakonczona i-tym klockiem. TO TO SAMO CO LIS 
def spadajaceklocki(T):
    def inclusion(A, B):
        return B[0] <= A[0] and B[1] >= A[1]
    N = len(T)
    F = [1 for _ in range (N)]
    for i in range (1, N):
        maxi = -float('inf')
        for j in range (i):
            if inclusion(T[i], T[j]): #T[i] zawiera sie w T[j]
                maxi = max(maxi, F[j])
        F[i] = maxi + 1
    return N - max(F)

T = [ [0, 5], [1, 4], [-3, 7], [2, 3], [2, 6], [4, 6], [2, 3] ]
T = [ (0, 10), (1, 10), (2, 6), (6, 7), (11, 20), (11, 19), (12, 18), (13, 19), (14, 20) ]
print(spadajaceklocki(T)) 