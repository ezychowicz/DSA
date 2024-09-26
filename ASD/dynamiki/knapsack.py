def knapsack(P, W, B): #ceny, wagi
    T = [i for i in range (len(P))]
    F = [[0 for _ in range (B + 1)] for __ in range (len(P))] #f(i,b) b w zakresie 0 do B
    
    taken = [[False for _ in range (B + 1)] for __ in range (len(P))]

    for b in range (W[0],B + 1):
        F[0][b] = P[0]
        taken[0][b] = True
    for i in range (1,len(P)):
        for b in range (B + 1):
            maxi = F[i - 1][b]
            if b >= W[i]:
                if maxi < F[i - 1][b - W[i]] + P[i]:
                    maxi = F[i - 1][b - W[i]] + P[i]
                    taken[i][b] = True
            F[i][b] = maxi

    def restore_sol1(): #z taken
        path = []
        b = B
        for i in range (len(W) - 1, -1,-1):
            if taken[i][b]:
                path.append(i)
                b -= W[i]
        path.reverse()
        print(path)
    restore_sol1()

    def restore_sol2(): #bez taken
        path = []
        i = len(W) - 1
        b = B 
        for i in range (len(W) -1 , 0, -1):
            if F[i][b] != F[i - 1][b]:
                path.append(i)
                b -= W[i]
                i -= 1
        if F[i][0] != 0: #ostatni rzad: czy wzielismy przedmiot 0
            path.append(i)
        path.reverse()
        print(path) 

    restore_sol2()
    return F[len(P) - 1][B]
    
P = [1, 4, 5, 7]
W = [1, 3, 4, 5]
B = 7 

print(knapsack(P,W,B))

