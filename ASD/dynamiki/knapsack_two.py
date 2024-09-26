def knapsack_2d(w, v, h, W, H):
    N = len(v)

    F = [[[0 for height in range (H + 1)] for weight in range (W + 1)] for i in range (N)]
    
    h0, w0, v0 = h[0], w[0], v[0]
    for weight in range (w0, W + 1):
        for height in range (h0, H + 1):
            F[0][weight][height] = v0
    
    for i in range (1, N):
        for weight in range (W + 1):
            for height in range (H + 1):
                if weight >= w[i] and height >= h[i]:
                    F[i][weight][height] = max(F[i - 1][weight - w[i]][height - h[i]] + v[i], F[i - 1][weight][height])                
                else:
                    F[i][weight][height] = F[i - 1][weight][height]
    return F[N - 1][W][H]

w = [2, 3, 4]
h = [3, 4, 5]
v = [3, 4, 5]
W = 7
H = 9
print(knapsack_2d(w,v,h,W,H))