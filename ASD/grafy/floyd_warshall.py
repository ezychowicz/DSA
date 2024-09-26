def floyd_warshall(G):
    def restore_path(P,a,b):
        i = b
        path = []
        while i != a:
            path.append(i)
            i = P[a][i]
        path.append(a)
        path.reverse()
        return path
    
    
    N = len(G)
    #convert
    P = [[None for _ in range (N)] for __ in range (N)]
    dist = [[float('inf') for _ in range (N)] for __ in range (N)]  
    for i in range (N):  #init dist and P
        for v in G[i]:
            dist[i][v[0]] = v[1]
            P[i][v[0]] = i
    for i in range (N):  #odleglosci od samych siebie
        dist[i][i] = 0
    
    for k in range (N):  #k ty wierzchołek spróbuj dołączyć do ścieżki między x a y
        for x in range (N):
            for y in range (N):
                if dist[x][k] + dist[k][y] < dist[x][y]:
                    dist[x][y] = dist[x][k] + dist[k][y]
                    P[x][y] = P[k][y]
    a = 3
    b = 5
    return restore_path(P,a,b)

graf = [[(1,1)],[(2,-5)],[(5,10)],[(5,15),(2,4),(4,-1),(1,1)],[(0,2)],[(0,-1),(4,2)]]

print(floyd_warshall(graf))