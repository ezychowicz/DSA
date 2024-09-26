#Emil Żychowicz
# Algorytm przechodzi przez listę T odpowiednio dodając elementy do jednego z kopców: min lub max (kopce są zrobione tutaj tak, aby 
# elementy w kopcu min były większe niż w kopcu max). Kluczowe jest utrzymanie, by na końcu każdej iteracji pętli oba
# kopce miały razem p elementów, a kopiec typu min miał k-1 elementów. Wówczas bowiem, k-ty największy element jest korzeniem kopca max. 
# Złożoność czasowa: O(nlogn). Złożoność pamięciowa: O(N) 
#from zad2testy import runtests
def left(i):
    return 2*i+1
def right(i):
    return 2*i+2
def parent(i):
    return (i-1)//2
def max_heapify(T,i):
    max_idx = i
    l = left(i)
    r = right(i)
    if l < len(T) and T[l][0] > T[max_idx][0]:
        max_idx = l
    if r < len(T) and T[r][0] > T[max_idx][0]:
        max_idx = r
    if i != max_idx:
        T[max_idx],T[i]  = T[i],T[max_idx]
        max_heapify(T,max_idx)

def heappop(T):
    N = len(T)
    popped = T[0]
    T[N-1],T[0] = T[0],T[N-1]
    T.pop()
    max_heapify(T,0)
    return popped

def push_up(T):
    N = len(T)
    i = N-1
    while i > 0 and T[parent(i)][0] < T[i][0]:
        T[parent(i)],T[i] = T[i],T[parent(i)]
        i = parent(i) 

def heappush(T,val):
    T.append(val)
    push_up(T)

def clear(T,T_bool):
    while T and T_bool[T[0][1]] == 0:
        heappop(T) 

def ksum(T, k, p):
    N = len(T)
    min_heap = []
    max_heap = []
    T_bool = [-1]*N
    if k == 1:
        for i in range (p):
            heappush(max_heap,(T[i],i))
        ans = max_heap[0][0]
        for i in range (p,N):
            T_bool[i-p] = 0
            clear(max_heap,T_bool)
            heappush(max_heap,(T[i],i))
            T_bool[i] = 2
            clear(max_heap,T_bool)
            ans += max_heap[0][0]
        return ans
    for i in range (k-1):
        heappush(min_heap,(-T[i],i))
        T_bool[i] = 1
    i = k-1
    while len(min_heap) + len(max_heap) < p:
        new = T[i]
        if new <= -min_heap[0][0]:
            heappush(max_heap,(new,i))
            T_bool[i] = 2
        else:
            tmp = heappop(min_heap)
            heappush(min_heap,(-new,i))
            T_bool[i] = 1
            heappush(max_heap,(-tmp[0],tmp[1]))
            T_bool[tmp[1]] = 2
        i += 1
    ans = max_heap[0][0]
    min_size = k-1
    for i in range (p,N):
        if T_bool[i-p] == 1:
            min_size -= 1
        T_bool[i-p] = 0
        clear(min_heap,T_bool)
        clear(max_heap,T_bool)
        new = T[i]
        if min_size < k-1:
            if new >= max_heap[0][0]:
                heappush(min_heap,(-new,i))
                T_bool[i] = 1
            else:
                tmp = heappop(max_heap)
                heappush(min_heap,(-tmp[0],tmp[1]))
                T_bool[tmp[1]] = 1
                heappush(max_heap,(new,i))
                T_bool[i] = 2
            min_size = k-1
        else:
            if new <= -min_heap[0][0]:
                heappush(max_heap,(new,i))
                T_bool[i] = 2
            else:
                tmp = heappop(min_heap)
                heappush(min_heap,(-new,i))
                T_bool[i] = 1
                heappush(max_heap,(-tmp[0],tmp[1]))
                T_bool[tmp[1]] = 2
        clear(min_heap,T_bool)
        clear(max_heap,T_bool)
        ans += max_heap[0][0]
    return ans


#runtests( ksum, all_tests=True )
