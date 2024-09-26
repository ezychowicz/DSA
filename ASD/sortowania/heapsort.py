#PLAYGROUND
import math

# algorytmy kopcowe pythonowo
def left(i):
    return 2*i+1
def right(i):
    return 2*i+2
def parent(i):
    return (i-1)//2

def heappush(T,val):
    T.append(val)
    push_up(T)

def push_up(T):
    N = len(T)
    i = N-1
    while i > 0 and T[parent(i)] < T[i]:
        T[parent(i)],T[i] = T[i],T[parent(i)]
        i = parent(i)

def heappop(T):
    N = len(T)
    T[0],T[N-1] = T[N-1],T[0]
    to_exctract = T.pop()
    return to_exctract

def max_heapify(T,i):
    max_idx = i
    l = left(i)
    r = right(i)
    if l < len(T) and T[l] > T[max_idx]:
        max_idx = l
    if r < len(T) and T[r] > T[max_idx]:
        max_idx = r
    if i != max_idx:
        T[max_idx],T[i] = T[i],T[max_idx]
        max_heapify(T,max_idx)

def build_heap(T):
    N = len(T)
    for i in range (parent(N-1),-1,-1):
        max_heapify(T,i)




def max_heapify_sort(T,i,n):
    max_idx = i
    l = left(i)
    r = right(i)
    if l < n and T[l] > T[max_idx]:
        max_idx = l
    if r < n and T[r] > T[max_idx]:
        max_idx = r
    if i != max_idx:
        T[max_idx],T[i] = T[i],T[max_idx]
        max_heapify_sort(T,max_idx,n)
def heapsort(T):
    build_heap(T)
    for i in range (len(T)-1,0,-1):
        T[i],T[0] = T[0],T[i]
        max_heapify_sort(T,0,i)
    return T



# algorytmy kopcowe w stylu C

def h_sort(T):
    n = len(T)
    def left(i):
        return 2*i+1
    def right(i):
        return 2*i+2
    def parent(i):
        return (i-1)//2
    def heappush(T,val): 
        nonlocal n
        n += 1
        T[n-1],T[0] = T[0],T[n-1]
        max_heapify(T,0,n)
    def heappop(T):
        nonlocal n
        to_exctract = T[0]
        T[n-1],T[0] = T[0],T[n-1]
        n -= 1
        return to_exctract
    def max_heapify(T,i):
        nonlocal n
        max_idx = i
        l = left(i)
        r = right(i)
        if l < n and T[l] > T[max_idx]:
            max_idx = l
        if r < n and T[r] > T[max_idx]:
            max_idx = r
        if i != max_idx:
            T[max_idx],T[i] = T[i],T[max_idx]
            max_heapify(T,max_idx)
    def build_heap(T):
        nonlocal n
        for i in range (parent(n-1),-1,-1):
            max_heapify(T,i)
    def heapsort(T):
        nonlocal n
        build_heap(T) 
        print(T)
        N = n
        for i in range (N-1,0,-1):
            T[0],T[i] = T[i],T[0]
            n = i
            max_heapify(T,0)
        return T
    return heapsort(T)
print(heapsort([2,4,6,4,2,5,8,52,7,5,3,78,4,34,7,43,7]))






# #scalanie k linked list w kopcu
# class Node:
#     def __init__(self,val=0,next=None):
#         self.val=val
#         self.next=next
# def min_heapify(T,i,h_size):
#     left=2*i+1
#     right=2*i+2
#     save=-1
#     if left<h_size and T[i].val>T[left].val:
#         save=left
#     if right<h_size and T[i].val>T[right].val:
#         if T[left].val>T[right].val:
#             save=right
#     if save!=-1:
#         T[save],T[i]=T[i],T[save]
#         min_heapify(T,save,h_size)

# def build_heap_min(T,h_size):
#     for i in range (h_size//2-1,-1,-1):
#         min_heapify(T,i,h_size)

# def wypisz(first):
#     while first!=None:
#         print(first.val,end=' ')
#         first=first.next

# def create(T):
#     first=head=Node()
#     for el in T:
#         head.next=Node(el)
#         head=head.next
#     return first.next

# def scal(T):
#     first=res=Node()
#     N=len(T)
#     build_heap_min(T,N)
#     while True:
#         res.next=T[0]
#         res=res.next
#         T[0]=T[0].next
#         if T[0]==None:
#             T[0]=Node(float('inf'))
#         min_heapify(T,0,N)
#         if T[0].val==float('inf'):
#             break
#     return  first.next
# wypisz(scal([create([1,5,9,13,17,21]),create([0,2,4,6,8,10]),create([15,16,17,18]),create([1,4,15]),create([-1,1,10,14,16,222])]))


# Merge k sorted arrays into one
def min_heapify(heap,i):
    min_idx = i
    l = left(i)
    r = right(i)
    h_size = len(heap)
    if l < h_size and heap[l][0] < heap[min_idx][0]:
        min_idx = l
    if r < h_size and heap[r][0] < heap[min_idx][0]:
        min_idx = r
    if i != min_idx:
        heap[min_idx],heap[i] = heap[i],heap[min_idx]
        min_heapify(heap,min_idx)  
def convert(T):
    size = 0
    for i in range (len(T)):
        size += len(T[i])
        T[i] = [T[i][0],0,T[i]]
    return size

def build_heap(heap):
    N = len(heap)
    for i in range (parent(N-1),-1,-1):
        min_heapify(heap,i)

def merge(T):
    size = convert(T)
    ans = [None]*size
    build_heap(T)
    i = 0
    while len(T) != 0:
        ans[i] = T[0][0]
        T[0][1] += 1
        if T[0][1] == len(T[0][2]):
            T[-1],T[0] = T[0],T[-1]
            T.pop()
        else:
            
            T[0][0] = T[0][2][T[0][1]]
            print(T[0][2][T[0][1]],T[0][0])
        min_heapify(T,0)
        i += 1
        print(T)
    return ans
# T = [[1,4,9,18],[5,8,9,10,11,15],[16,43,77],[1,5,111],[16,18,19],[41,43,45,77],[1,2,3,4,5,66]]
# print(merge(T))

# Find the smallest range with at least one element from each of the k N-element sorted arrays. (start,end) 

# def s_range(T):
#     h_size = len(T)
#     def build_heap(T):
#         N = len(T)
#         heap = [None]*N
#         maxi = -float('inf')
#         for i in range (len(T)):
#             heap[i] = [T[i][0],i,0] #wartosc,ktora tablica,aktualny indeks
#             maxi = max(T[i][0],maxi)
#         for i in range (parent(N-1),-1,-1):
#             min_heapify(heap,0)
#         return heap,maxi
#     def min_heapify(T,i):
#         nonlocal h_size
#         min_idx = i
#         l = left(i)
#         r = right(i)
#         if l < h_size and T[l][0] < T[min_idx][0]:
#             min_idx = l
#         if r <h_size and T[r][0] < T[min_idx][0]:
#             min_idx = r
#         if i != min_idx:
#             T[min_idx],T[i] = T[i],T[min_idx]
#             min_heapify(T,min_idx)
#     def smallest_range(T):
#         heap_info = build_heap(T)
#         heap = heap_info[0]
#         maxi = heap_info[1]
#         min_range = float('inf')
#         flag = False
#         save = None
#         while True:
#             print(maxi)
#             if maxi - heap[0][0] < min_range:
#                 min_range = maxi - heap[0][0]
#                 save = (heap[0][0],maxi)
#             min_range = min(maxi - heap[0][0],min_range)
#             if heap[0][2] == len(T[heap[0][1]])-1:
#                 break
#             else:
#                 heap[0][2] += 1
#                 heap[0][0] = T[heap[0][1]][heap[0][2]]
#                 maxi = max(maxi,heap[0][0])
#                 min_heapify(heap,0)
#         return save
#     return smallest_range(arr)
#arr = [[1, 3, 5, 7, 9], [0, 2, 4, 6, 8], [2, 3, 5, 7, 11]]
#print(s_range(arr))
    

# Sort k-chaotic array using heap.

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order. (Leetcode347)

# Find k closest elements. Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order. (Leetcode658)