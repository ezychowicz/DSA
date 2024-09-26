#f(i,k) - minimalna liczba skokow z i-tej pozycji do N - 1, zaczynając na wejsciu do i-tej pozycji z k energii
#odp: min(k)(f(0,k))
#f(i,k) = min(j > i and k + A[i] >= j - i)(f(j, k + A[i] - (j - i))) + 1
#for all k: f(n,k) = 0
def glodnazaba(A):
    N = len(A)
    MAX_ENERGY = sum(A)
    F = [[float('inf') for _ in range (MAX_ENERGY + 1)] for __ in range (N)]
    checked = [[False for _ in range (MAX_ENERGY + 1)] for __ in range (N)]
    for i in range (MAX_ENERGY + 1):
        F[N - 1][i] = 0
        checked[N - 1][i] = True
    def f(i,k):
        if checked[i][k]:
            return F[i][k]
        mini = float('inf')
        for j in range (i + 1, N):
            if k + A[i] >= j - i:
                mini = min(mini, f(j, k + A[i] - (j - i)))
        F[i][k] = mini + 1
        checked[i][k] = True
        return F[i][k]
    f(0,0) #zaczynamy w zerze z zerem energii
    return min(F[0])

def iteracyjnie(T):
    N = len(A)
    MAX_ENERGY = sum(A)
    F = [[float('inf') for _ in range (MAX_ENERGY + 1)] for __ in range (N)]
    for i in range (MAX_ENERGY + 1):
        F[N - 1][i] = 0
 
    for i in range (N - 2, -1 , -1): #tutaj liczymy od tylu
        for k in range (MAX_ENERGY + 1):
            mini = float('inf')
            for j in range (N - 1, i, -1):
                if k + A[i] - (j - i) > MAX_ENERGY: #taka energia jest nieosiagalna w zaden sposob
                    continue
                if k + A[i] >= j - i:
                    mini = min(mini, F[j][k + A[i] - (j - i)])
            F[i][k] = mini + 1
        
    return F[0][0]



A = [2, 2, 1, 0, 0, 0]
print( iteracyjnie(A) ) # 3
print(glodnazaba(A))
A = [2, 3, 1, 1, 2, 0]
print( iteracyjnie(A) ) # 2
print(glodnazaba(A))
A = [5, 0, 0, 0]
print( iteracyjnie(A) ) # 1
print(glodnazaba(A))