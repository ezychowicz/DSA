def counting_sort(T):
    k = 0
    for i in range (len(T)):
        k = max(k,len(T[i]))
    count = [0]*k
    new = [None]*len(T)
    for i in range (len(T)):
        count[len(T[i])-1] += 1
    for i in range (1,k):
        count[i] += count[i-1]
    for i in range (len(T)-1,-1,-1):
        new[count[len(T[i])-1] - 1] = T[i]
        count[len(T[i])-1] -= 1
    return new 



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

print(sorting(["abcd","ncd","afsda","fsd","rdgdrdg","rdfrdgrgr","sf"])) #sortuje w odp dlugosciach



#proper sort
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
T = ["abcd","ncd","afsda","fsd","rdgdrdg","rdfrdgrgr","sf"]
sorting(T)
print(T)
print(sorted(["abcd","ncd","afsda","fsd","rdgdrdg","rdfrdgrgr","sf"]))