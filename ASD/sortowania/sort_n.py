def reverse(T):
    N = len(T)
    for i in range (N//2):
        T[i],T[N-i-1] = T[N-i-1],T[i]

#countign sort malejąco
def counting_sort(T,k):
    count = [0]*k
    new = [None]*(len(T))
    for i in range (len(T)):
        count[T[i]] += 1
    for i in range (k-2,-1,-1):
        count[i] += count[i+1]
    for i in range (len(T)-1,-1,-1):
        new[count[T[i]] - 1] = T[i]
        count[T[i]] -= 1
    return new

def counting_sort(T,k): #zwykly
    count = [0]*k
    new = [None]*(len(T))
    for i in range (len(T)):
        count[T[i]] += 1
    for i in range (1, k):
        count[i] += count[i-1]
    for i in range (len(T)-1,-1,-1):
        new[count[T[i]] - 1] = T[i]
        count[T[i]] -= 1
    return new

print(counting_sort([3,2,1,1,0],4))

#RADIX - NAJPIERW DLUGOSCIAMI POTEM RADIX NA FIXED LENGTHS, counting sort/quicksort na dlugosciach do napisania
def counting_sort(T): pass #na dlugosciach
def counting_sort2(T,k,pos):
    count = [0]*k
    new = [None]*len(T)
    for i in range (len(T)):
        count[ord(T[i][pos]) - ord('a')] += 1
    for i in range (1,k):
        count[i] += count[i-1]
    for i in range (len(T)-1,-1,-1):
        new[count[ord(T[i][pos]) - ord('a')] - 1] = T[i]
        count[ord(T[i][pos]) - ord('a')] -= 1
    return new 

def radix_sort(T):
    k = len(T[0])
    for i in range (k-1,-1,-1):
        T = counting_sort2(T,ord('z') - ord('a') + 1,i)
    return T

def sorting(T):
    T = counting_sort(T)
    N = len(T)
    start = 0
    cnt = 0
    for i in range (1,N):
        if len(T[i]) != len(T[i-1]):
            B = radix_sort(T[start:i])
            print(B)
            for el in B:
                T[cnt] = el
                cnt += 1
            start = i
    return T

#PROPER RADIX ON STRINGS
def sorting(T):
    def val(word,pos):
        if pos >= len(word):
            return 0
        return ord(word[pos]) - ord('a') + 1
    def partition(T,p,r,pos): #counting_sort
        T_copy = T[p:(r+1)]
        print("sort:",T_copy,"by position:",pos)
        count = [0]*(ord('z') - ord('a') + 2)
        for i in range (len(T_copy)):
            count[val(T_copy[i],pos)] += 1
        for i in range (1,len(count)):
            count[i] += count[i-1]
        parts = count[::]
        for i in range (len(T_copy)-1,-1,-1):
            T[p + count[val(T_copy[i],pos)] - 1] = T_copy[i]
            count[val(T_copy[i],pos)] -= 1
        return parts
    def max_length(T):
        maxi = 0
        for i in range (len(T)):
            maxi = max(maxi,len(T[i]))
        return maxi
    def radix_sort(T,p,r,pos):
        if p >= r or pos >= max_length(T[p:(r+1)]):
            return
        parts = partition(T,p,r,pos)
        j = p + parts[0]
        print(T[p:r+1],parts)
        for i in range(1,len(parts)):
            radix_sort(T,j,p + parts[i]-1,pos+1)
            j = p + parts[i]
    radix_sort(T,0,len(T)-1,0)


#BUCKET SORT
def inserting(T,key):
    i = 0
    while i < len(T) and T[i] < key:
        i += 1
    T.insert(i,key)


def bucket_sort(T,k): #w szczegolnosci k zazwyczaj rowna sie N
    maxi = max(T)
    N = len(T)
    buckets = [[] for _ in range (k+1)]
    for el in T:
        inserting(buckets[int((el/maxi)*k)],el)
    res = [None]*N
    i = 0
    for bucket in buckets:
        for el in bucket:
            res[i] = el
            i += 1
    return res
