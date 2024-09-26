import random
def partition(T,p,r):
    i = p-1
    j = p
    x = T[r]
    while j < r:
        if T[j] < x:
            i += 1
            T[i],T[j] = T[j],T[i]
        j += 1
    T[i+1],T[r] = T[r],T[i+1]
    return i+1
#quicksort o złożoności pamięciowej O(logn)   S(n) = c + S(n/2) = 2c + S(n/4) = ... = ic + S(n/2^i) i=logn max
def quicksort_mem(T,p,r):
    while p < r:
        q = partition(T,p,r)
        if r-q >= r-p:
            quicksort_mem(T,p,q-1)
            p = q+1
        else:
            quicksort_mem(T,q+1,r)
            r = q-1

# T = [random.randint(1,100) for i in range (100)]
# quicksort(T,0,len(T)-1)

#insert do kopca

# def parent(i):
#     return (i-1)//2
# def increase(T,i,key):
#     T[i] = key
#     while i>0 and T[parent(i)] <= T[i]:
#         T[parent(i)],T[i] = T[i],T[parent(i)]
#         i = parent(i)
# def insert(T,key):
#     T.append(-float('inf'))
#     increase(T,len(T)-1,key)

#quicksort iteracyjnie

def quicksort_iter(T):
    p = 0
    r = len(T)-1
    stack = [[p,r]]
    while stack != []:
        p,r = stack[-1][0],stack[-1][1]
        q = partition(T,p,r)
        stack.pop()
        if p < q:
            stack.append([p,q-1])
        if q < r:
            stack.append([q+1,r])



#T = [random.randint(1,100) for i in range (100)]
# quicksort_iter(T)
# print(T)


#CWICZENIA START


#implementacja quicksorta, żeby nie używał więcej niż O(logn) pamięci


#implementacja QS bez rekurencji
#1 i 2
def qs_iter_mem(T,p,r):
    stack = [[p,r]]
    while len(stack) != 0:
        p,r = stack[-1][0],stack[-1][1]
        stack.pop()
        q = partition(T,p,r)
        if q-p <= r-q:
            if q < r:
                stack.append([q+1,r])
            if p < q:
                stack.append([p,q-1])
        else:
            if p < q:
                stack.append([p,q-1])
            if q < r:
                stack.append([q+1,r])
    #na stos najpierw dodajemy dluzszy fragment potem krotszy (najpierw zajmiemy sie tymi krotszymi)
    return T
#print(qs_iter_mem(T,0,len(T)-1))


#algorytm scalający k list

#struktura danych która wykonuje: insert, remove Median w czasie O(logn)
# struktura 1: dwa kopce - min i max: k-1 najmniejszych wartości w maxie, reszta w min
# def left(i):
#     return 2*i+1
# def right(i):
#     return 2*i+2
# def parent(i):
#     return (i-1)//2
# def max_heapify(T,i):
#     max_idx = i
#     l = left(i)
#     r = right(i)
#     if l < len(T) and T[l] > T[max_idx]:
#         max_idx = l
#     if r < len(T) and T[r] > T[max_idx]:
#         max_idx = r
#     if i != max_idx:
#         T[i],T[max_idx] = T[max_idx],T[i]
#         max_heapify(T,max_idx)
# def heappush(T,val):
#     T.append(val)
#     push_up(T)
# def heappop(T):
#     T[0],T[len(T)-1] = T[len(T)-1],T[0]
#     k = T.pop()
#     max_heapify(T,0)
#     return k 
# def push_up(T):
#     N = len(T)
#     i = N-1
#     while i > 0 and T[parent(i)] < T[i]:
#         T[parent(i)],T[i] = T[i],T[parent(i)]
#         i = parent(i)
# def repair(min_heap,max_heap):
#     if len(min_heap) < len(max_heap):
#         to_move = heappop(max_heap)
#         heappush(min_heap,-to_move)
# def insert(val,min_heap,max_heap):
#     if len(min_heap) == len(max_heap) == 0:
#         heappush(min_heap,-val) 
#         return
    
#     if (len(min_heap) + len(max_heap))%2 == 0:
#         if val >= max_heap[0]:
#             heappush(min_heap,-val)
#         else:
#             tmp = heappop(max_heap)
#             heappush(max_heap,val)
#             heappush(min_heap,-tmp)
#     else:
#         if val <= -min_heap[0]:
#             heappush(max_heap,val)
#         else:
#             tmp = heappop(min_heap)
#             heappush(min_heap,-val)
#             heappush(max_heap,-tmp)
# def remove_median(min_heap,max_heap):
#     median = -heappop(min_heap)
#     repair(min_heap,max_heap)
#     return median
# min_heap = []
# max_heap = []
# insert(4,min_heap,max_heap)
# insert(7,min_heap,max_heap)
# insert(3,min_heap,max_heap)
# insert(8,min_heap,max_heap)
#print(min_heap,max_heap)
#print(remove_median(min_heap,max_heap))
#print(min_heap,max_heap)


#struktura 2: lista dwukierunkowa (nie jest logn) 

class Node():
    def __init__(self,val = None,next = None,prev = None):
        self.val = val
        self.next = next
        self.prev = prev

# def insert(p,key):
#     if p == None:
#         return Node(key)
#     dummy = Node(-float('inf'),p,None)
#     p.prev = dummy
#     p = dummy
#     while p.next != None and p.next.val < key:
#         p = p.next
#     if p.next == None:
#         p.next = Node(key,None,p)
#         return dummy.next
#     new = Node(key,p.next,p)
#     p.next = new
#     p.next.prev = new 
#     return dummy.next

def print_DLL(p):
    if p == None:
        print(None)
    while p.next != None:
        print(p.val,"<-> ",end='')
        p = p.next
    print(p.val)


def insert_between(p1,p2,key):
    new = Node(key)
    if p1 == None:
        p2.prev = new
        new.next = p2
    if p2 == None:
        p1.next = new
        new.prev = p1

def insert(median,key,length):
    if median == None:
        return Node(key)
    if key < median.val:
        insert_between(median.prev,median,key)
        if length%2 == 0:
            return median.prev
        return median
    else:
        insert_between(median,median.next,key)
        if length%2 == 0:
            return median
        return median.next
    
def remove_median(median):
    if median.next == None:
        median = median.prev
        median.next = None
        return
    median.prev = None
    median.next = None
    return median

p = None
p = insert(p,0,0)
print_DLL(p)
p = insert(p,1,1)
print_DLL(p)
p = insert(p,-1,2)
print_DLL(p)