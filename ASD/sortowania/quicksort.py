import random
#a) partition Lomuto
def partition(T,p,r):
    i = p-1
    j = p
    x = T[r]
    while j < r:
        if T[j] <= x:
            i += 1
            T[i],T[j] = T[j],T[i]
        j += 1
    T[i+1],T[r] = T[r],T[i+1]
    return i+1

def quicksort(T,p,r):
    if r <= p:
        return
    q = partition(T,p,r)
    quicksort(T,p,q-1)
    quicksort(T,q+1,r)

def select(T,p,r,k):
    if p == r:
        return T[p]
    q = partition(T,p,r)
    if q == k:
        return T[q]
    elif q < k:
        return select(T,q+1,r,k)
    else:
        return select(T,p,q-1,k)
    

#d) randomized quicksort
def r_partition(T,p,r):
    i = random.randint(p,r)
    T[i],T[r] = T[r],T[i]
    return partition(T,p,r)
def r_quicksort(T,p,r):
    if r <= p:
        return
    q = r_partition(T,p,r)
    r_quicksort(T,p,q-1)
    r_quicksort(T,q+1,r)

# T = [random.randint(1,100) for i in range (100)]
# r_quicksort(T,0,len(T)-1)
# print(T)

def quicker_partition(T,p,r):
    i = p-1
    j = p
    k = r
    x = T[r]
    while j <= k:
        if T[j] < x:
            i += 1
            T[j],T[i] = T[i],T[j]
            j += 1
        elif T[j] == x:
            j += 1
        else:
            T[k],T[j] = T[j],T[k]
            k -= 1
    return i, j 
def quicker_sort(T,p,r):
    if p >= r:
        return
    parts = quicker_partition(T,p,r)
    quicksort(T,p,parts[0])
    quicksort(T,parts[1],r)

T = [random.randint(1,2) for i in range (20)]
quicker_sort(T,0,19)

print(T)




#b) partition Hoare
def partition_hoare(T,p,r):
    i = p-1
    j = r+1
    x = T[p]
    while True:
        i += 1
        while T[i] <= x:
            i += 1
        j -= 1
        while T[j] >= x:
            j -= 1
        if i >= j:
            return j
        T[i],T[j] = T[j],T[i]