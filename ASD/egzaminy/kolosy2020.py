#zad1
'''
def is_prettier(A,B):
    if A[0] > B[0]:
        return True
    elif A[0] < B[0]:
        return False
    return A[1] <= B[1] 
def count(a):
    a_save = a
    if a == 0:
        return (1,0,0) 
    count = [0]*10
    while a > 0:
        count[a%10] += 1
        a //= 10
    ones,mores = 0,0
    for el in count:
        if el == 1:
            ones += 1
        elif el > 1:
            mores += 1
    return ones,mores,a_save
def convert(T):
    N = len(T)
    for i in range (N):
        T[i] = count(T[i])

def merge(T1,T2):
    T = [None]*(len(T1) + len(T2))
    T1.append((-float('inf'),0,0))
    T2.append((-float('inf'),0,0))
    i,j,k = 0,0,0
    while T1[i][0] != -float('inf') or T2[j][0] != -float('inf'):
        if is_prettier(T1[i],T2[j]):
            T[k] = T1[i]
            i += 1
        else:
            T[k] = T2[j]
            j += 1
        k += 1
    return T
def mergesort(T):
    if len(T) == 1:
        return T
    mid = len(T)//2
    T1 = mergesort(T[:mid])
    T2 = mergesort(T[mid:])
    return merge(T1,T2)
    
def pretty_sort(T):
    N = len(T)
    convert(T)
    T = mergesort(T)
    for i in range (N):
        T[i] = T[i][2]
    return T

T = [67333,123,114577,455,1266,2344]
print(pretty_sort(T))
'''
#zad2
def two_Sum(T,x,idx):
    i = 0
    j = len(T) - 1
    while i != j:
        if T[i] > x:
            return False
        if j == idx:
            j -= 1
            continue
        if i == idx:
            i += 1
            continue
        if T[i] + T[j] > x:
            j -= 1
        elif T[i] + T[j] < x:
            i += 1
        else:
            return True
    return False


def is_sum(T):
    T = sorted(T)
    N = len(T)
    for i in range (N):
        if not two_Sum(T,T[i],i):
            return False
    return True
import random
print(is_sum([-2,-2,0,2,2,3]))