#f(w,k) = T[w][k] + min(f(w - 1, k), f(w, k - 1))
def min_cost(T):
    F = [[float('inf') for _ in range (len(T))] for __ in range (len(T))]
    F[0][0] = T[0][0]
    to_check = ((-1,0),(0,-1))
    N = len(T)
    for i in range (N):
        for j in range (N):
            mini = float('inf')
            for el in to_check:
                if 0 <= i + el[0] < N and 0 <= j + el[1] < N:
                    mini = min(F[i + el[0]][j + el[1]], mini)
            if i == 0 and j == 0: #bo wtedy akurat mini = inf
                continue
            F[i][j] = T[i][j] + mini
    return F[N - 1][N - 1]

