#sortowania liniowe
def counting_sort(T,k):
    N = len(T)
    counter = [0]*(k)  #tutaj spoko gdy sortujemy liczby od zera, bo jak nie to trzeba jakies przesuniecia
    sorted = [0]*N
    for i in range (N):
        counter[T[i]] += 1
    for i in range (1,k):
        counter[i] += counter[i-1]
    for i in range (N-1,-1,-1):
        sorted[counter[T[i]]-1] = T[i]
        counter[T[i]] -= 1
    return sorted
import random
T = [random.randint(0,10000) for i in range (15)]
k = 11
#print(counting_sort(T,k))
import math
def exc_dig(a,dig):
    return (a//10**(dig))%10

def counting_sort2(T,k,dig):
    N = len(T)
    counter = [0]*(k)  #tutaj spoko gdy sortujemy liczby od zera, bo jak nie to trzeba jakies przesuniecia
    sorted = [0]*N
    for i in range (N):
        counter[exc_dig(T[i],dig)] += 1
    for i in range (1,k):
        counter[i] += counter[i-1]
    for i in range (N-1,-1,-1):
        sorted[counter[exc_dig(T[i],dig)]-1] = T[i]
        counter[exc_dig(T[i],dig)] -= 1
    return sorted

def num_length(num):
    return math.ceil(math.log(num,10)) + 1

# def radix_sort(T):
#     maxi = max(T)
#     length = num_length(maxi)
#     for i in range (length):
#         T = counting_sort2(T,10,i)
#     return T

#print(radix_sort(T))
class Node:
    def __init__(self,val = None,next = None):
        self.next = next
        self.val = val
# def insert(dummy,key):
#     p = dummy
#     while p.next != None and p.next.val < key:
#         p = p.next
#     if p.next == None:
#         p.next = Node(key)
#     else:
#         new = Node(key,p.next)
#         p.next = new
# def wypisz(first):
#     while first!=None:
#         print(first.val,end=' ')
#         first=first.next
#     print("")
# def bucket_sort(T):
#     LL = [Node() for i in range (10)]
#     for el in T:
#         insert(LL[math.floor(el*10)],el)
#     sorted = [0]*len(T)
#     i = 0
#     for j in range (10):
#         p = LL[j]
#         p = p.next
#         while p != None:
#             sorted[i] = p.val
#             p = p.next
#             i += 1 
#     return sorted
# import numpy as np
#T = np.random.uniform(0,1,100)
#print(bucket_sort(T))

# Cwiczenia START


#zad1. Tablica n liczb o liczbach z zakresu 0-n^2-1. Posortować.
def conv(a,pos,n):
    if pos == 0:
        return a%n 
    else:
        return (a//n)%n
def counting_sort(T,pos):
    n = len(T)
    count = [0]*n
    B = [None]*n
    for i in range (n):
        count[conv(T[i],pos,n)] += 1
    for i in range (1,n):
        count[i] += count[i-1]
    for i in range (n-1,-1,-1):
        B[count[conv(T[i],pos,n)]-1] = T[i]
        count[conv(T[i],pos,n)] -= 1
    return B
def radix_sort(T):
    T = counting_sort(T,1)
    return counting_sort(T,0)

#print(radix_sort(T))
#zamiana na liczby o podstawie n
#zad2. Tablica n liczb mająca O(logn) róznych wartosci.
def bin_search(T,key):
    if not T:
        return key
    l = 0
    r = len(T) - 1
    while l <= r:
        mid = (l+r)//2
        if T[mid] == key:
            return mid
        if T[mid] < key:
            if mid == len(T) - 1:
                return mid+1
            l = mid + 1
        else:
            if mid == 0:
                return mid
            if T[mid-1] <= key:
                return mid
            r = mid - 1
#ogarnac tego bin searcha jeszcze
def bin_search(T,key):
    left = 0
    right = len(T) #bo gdy insetujemy na ostatnie miejsce to ma zwrocic len(T)
    while left < right:
        mid = (left+right)//2
        if T[mid] < key:
            left = mid + 1
        elif T[mid] >= key:
            right = mid
    return left
def costam(T):
    n = len(T)
    B = []
    for i in range (n):
        k = bin_search(B,T[i])
        B.insert(k,T[i])
    return B
T = [2,577,4,4,2,44]
print(T)
print(costam(T))
#bin_search

#zad3. Inwersje w tablicy.
#zrobione na cw. 2
#zad4. Funkcja sprawdzająca czy dwa słowa są anagramami.
def anagram(w1,w2):  #O(n+k)
    if len(w1) != len(w2):
        return False
    T = [0]*(ord('z')-ord('a')+1)
    for i in range (len(w1)):
        T[ord(w1[i])-ord('a')] += 1
        T[ord(w2[i])-ord('a')] -= 1
    for i in range (len(T)):
        if T[i] != 0:
            return False
    return True

#print(anagram("look","kool"))
#wariant 2
import random
count = [random.randint(1000,10000) for i in range (100)]
def anagram(w1,w2,count):
    if len(w1) != len(w2):
        return False
    for el in w1:
        count[ord(el)] = 0
    for i in range (len(w1)):
        count[ord(w1[i])] += 1
        count[ord(w2[i])] -= 1
    for el in w1:
        if count[ord(el)] != 0:
            return False
    return True

#1)zerujemy tylko counter w indeksach wskazywanych przez wyrazy
#2)przechodzimy przez slowa i odpowiednio dodajemy w odpowiednich indeksach
#3)sprawdzamy czy są same zera (znowu idąc po indeksach ze słów)

#zad5. Znalezc najkrotszy podciag zawierajacy kazdą z liczb k w ciągu o elementach ze zbioru k liczb.
def shortest_subs(T,k):
    N = len(T)
    state = [0]*k
    cnt = 0
    for i in range (k):
        if state[T[i]] == 0:
            cnt += 1
        state[T[i]] += 1
    if cnt == k:
        return k
    mini = float('inf')
    i = 0
    j = k-1
    while j < N-1:
        if cnt == k:
            mini = min(mini,j-i+1)
            state[T[i]] -= 1
            if state[T[i]] == 0:
                cnt -= 1
            i += 1
        else:
            j += 1
            if state[T[j]] == 0:
                cnt += 1
            state[T[j]] += 1
    if state[T[j]] == 0:
        cnt += 1
    state[T[j]] += 1
    while cnt == k:
        mini = min(mini,j-i+1)
        state[T[i]] -= 1
        if state[T[i]] == 0:
            cnt -= 1
        i += 1
    return mini
#print(shortest_subs([1,2,1,1,1,1,1,0,1,0,1,0,0,0,0,1,1,1,1,2,1,2,1,0],3))

#zad6. Tablica n różnych liczb, które po posortowaniu byłyby koło siebie i których różnica jest maksymalna. 
# def push(T,i):
#     while i < len(T):
#         T[i],key = key,T[i]
#         i += 1
# def insert(T,key):
#     if not T:
#         return [key]
#     T.append(None)
#     i = 0
#     while T[i] < key:
#         i += 1
#     push(T,i,key)    
# def fill_buckets(T):
#     n = len(T)
#     T_range = max(T) - min(T)
#     step = T_range/n
#     buckets = [[] for i in range (n)]
#     for i in range (n):
#         insert(buckets[],T[i])
#     print(buckets)
# print(fill_buckets([1,8,3,2,6,8,4,5,8,4,1]))