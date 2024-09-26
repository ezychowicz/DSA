import random
class Node:
    def __init__(self,val=None,next=None):
        self.val = val
        self.next = next
def create(T):  
    head=Node()
    dummy=head
    for el in T:
        head.next=Node(el)
        head=head.next
    return dummy.next
def wypisz(first):
    while first!=None:
        print(first.val,end=' ')
        first=first.next
    print("")



def insertion_sort(T):
    N=len(T)
    for i in range (1,N):
        j=i-1
        key=T[i]
        while j>=0 and key<T[j]:
            T[j+1] = T[j]  
            j-=1
        T[j+1]=key
        print(T)
    return T

print(insertion_sort([7,6,3,7,6,59,4]))
def insertion_sort(T):
    N = len(T)
    for i in range (1,N):
        key = T[i]
        i -= 1
        while i >= 0 and T[i] > key:
            T[i+1],T[i] = T[i],T[i+1]
            i -= 1
        #T[i+1] = key to sposób drugi - zamiast swapować w L8: T[i+1] = T[i]
    return 
print(insertion_sort([7,4,2,8,3,5]))





def bubble_sort(T):
    flag=True
    N=len(T)
    while flag:
        flag=False
        for i in range (N-1):
            if T[i+1]<T[i]:
                T[i],T[i+1]=T[i+1],T[i]
                flag=True
    return T

print(bubble_sort([4,6,32,7,4,3,7]))






def selection_sort(T):
    N = len(T)
    for i in range (N-1):
        save_idx = i
        mini = T[i] 
        for j in range (i+1, N):
            if mini > T[j]:
                save_idx = j
                mini = T[j]
        if save_idx != i:
            T[i],T[save_idx] = T[save_idx],T[i]
    return T
print(selection_sort(([7,4,2,8,3,5])))





def exctract_min(p): #p jest niezmienialne, wartownik
    mini = float('inf')
    dummy = p
    while p.next != None:
        if p.next.val < mini:
            prev_min = p
            min_node = p.next
            min_next = p.next.next
            mini = p.next.val
        p = p.next
    prev_min.next = min_next
    to_save = dummy.next  #do tego dołącze min_node, bo to jest wskaznik na listę wejsciową (do tej funkcji) tylko juz bez min_nodea (w sumie moglbym tutaj)
    return min_node, to_save


def selection_sort_list(p): 
    dummy = Node()
    dummy.next = p
    while p.next != None:
        exc = exctract_min(p)
        p.next = exc[0]
        exc[0].next = exc[1]
        p = p.next
    return dummy.next

p = create([6,3,2,7,2,7,41,1])
wypisz(selection_sort_list(p))





