#O(V!) - wszystkie scieżki
# from zad4testy import runtests

# def convert(L):
#     size = 0
#     for i in range (len(L)):
#         size = max(size,L[i][1])
#     G = [[] for _ in range (size+1)]
#     for i in range (len(L)):
#         G[L[i][0]].append((L[i][1],L[i][2]))
#         G[L[i][1]].append((L[i][0],L[i][2]))
#     return G

# def intersect(A,B):
#     return (max(A[0],B[0]),min(A[1],B[1]))
# def Flight(L,x,y,t):
#     G = convert(L)
#     visited = [False]*(len(G))
#     def DFSVisit(i,bound):
#         if bound[0] > bound[1]:
#             # print("gedagadi")
#             return False
#         if i[0] == y:
#             return True
#         visited[i[0]] = True
#         for v in G[i[0]]:
#             if not visited[v[0]]:
#                 a = DFSVisit(v,intersect(bound,(v[1] - t,v[1] + t)))
#                 if a:
#                     return a
#                 visited[v[0]] = False
#         return False
    
#     return DFSVisit((x,0),(-float('inf'),float('inf')))


#O(E(V+E))
#gdyby chciec bez list siasiedztwa:
    # def DFS_check(i,h):
    #     if i == y:
    #         return True
    #     visited[i] = True
    #     for edge in L:
    #         if edge[0] == i and not visited[edge[1]] and abs(edge[2] - h) <= t:
    #             is_found = DFS_check(edge[1],h)
    #             if is_found:
    #                 return True
    #     return False
#from zad4testy import runtests
def Flight(L,x,y,t):
    def convert(L):
        size = 0
        for i in range (len(L)):
            size = max(size,L[i][1])
        G = [[] for _ in range (size+1)]
        for i in range (len(L)):
            G[L[i][0]].append((L[i][1],L[i][2]))
            G[L[i][1]].append((L[i][0],L[i][2]))
        return G
    
    G = convert(L)

    def DFS_check(i,h):
        if i == y:
            return True
        visited[i] = True
        for v in G[i]:
            if not visited[v[0]] and abs(v[1] - h) <= t:
                is_found = DFS_check(v[0],h)
                if is_found:
                    return True
        return False

    for el in L:
        visited = [False]*(len(G))
        if DFS_check(x,el[2] - t) or DFS_check(x,el[2] + t):
            return True
    return False

#runtests( Flight, all_tests = True )
