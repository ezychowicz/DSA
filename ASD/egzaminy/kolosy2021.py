# def partition(T,p,r):
#     i = p-1
#     j = p
#     while j < r:
#         if T[j] <= T[r]:
#             i += 1
#             T[j],T[i] = T[i],T[j]
#         j += 1
#     T[i+1],T[r] = T[r],T[i+1]
#     return i+1
# def q_select(T,p,r,k):
#     q = partition(T,p,r)
#     if q == k:
#         return T[q]
#     elif q < k:
#         return q_select(T,q+1,r,k)
#     else:
#         return q_select(T,p,q-1,k)

# def check(num,a,b):
#     if num >= a and num <= b:
#         return 1
#     elif num < a:
#         return 0
#     else:
#         return 2
    
# def partition_012(T,a,b):
#     i = -1
#     j = 0
#     k = len(T) - 1
#     while j <= k:
#         if check(T[j],a,b) == 0:
#             i += 1
#             T[i],T[j] = T[j],T[i]
#             j += 1
#         elif check(T[j],a,b) == 1:
#             j +=1 
#         else:
#             T[k],T[j] = T[j],T[k]
#             k -= 1

# def fill_board(T,L,N):
#     cnt = 0
#     for i in range (1,N):
#         for j in range (i):
#             T[i][j] = L[cnt] 
#             cnt += 1
#     for i in range (N):
#         T[i][i] = L[cnt]
#         cnt += 1
#     for i in range (N-1):
#         for j in range (i+1,N):
#             T[i][j] = L[cnt]
#             cnt += 1

# def Median(T):
#     N = len(T)
#     L = [None]*N**2
#     cnt = 0
#     for i in range (len(T)):
#         for j in range (len(T[i])):
#             L[cnt] = T[i][j]
#             cnt += 1
#     a = q_select(L,0,N**2-1,(N**2-N)//2)
#     b = q_select(L,0,N**2-1,(N**2-N)//2 + N-1)
#     partition_012(L,a,b)
#     print(L,a,b)
#     fill_board(T,L,N)
#     print(*T,sep = '\n')

T = [
[ 2, 3, 5],
[ 7,11,13],
[17,19,23] ]
#Median(T)

#in-place:

def partition(T,p,r,N):
    i = p-1
    j = p
    while j < r:
        if T[j//N][j%N] <= T[r//N][r%N]:
            i += 1
            T[j//N][j%N],T[i//N][i%N] = T[i//N][i%N],T[j//N][j%N]
        j += 1
    T[(i+1)//N][(i+1)%N],T[r//N][r%N] = T[r//N][r%N],T[(i+1)//N][(i+1)%N]
    return i+1
def q_select(T,p,r,k):
    q = partition(T,p,r,len(T))
    if q == k:
        return T[q//len(T)][q%len(T)]
    elif q < k:
        return q_select(T,q+1,r,k)
    else:
        return q_select(T,p,q-1,k)

def check(num,a,b):
    if num >= a and num <= b:
        return 1
    elif num < a:
        return 0
    else:
        return 2
    
def partition_012(T,a,b):
    #problemy najmana
    pass
def Median(T):
    N = len(T)
    a = q_select(T,0,N**2-1,(N**2-N)//2)
    b = q_select(T,0,N**2-1,(N**2-N)//2 + N-1)
    partition_012(T,a,b)
    #fill_board(T,L,N)
    print(a,b)
    print(*T,sep='\n')


T = [ [13,19,23],
[ 3, 7,17],
[ 5, 2,11] ]
print(Median(T))
