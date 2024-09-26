#sortowanie list jednokierunkowych

class Node:
    def __init__(self, val=None, next=None):
        self.next=next
        self.val=val

#a) wstawianie
#b) insertion sort
#c) wyjmowanie el. max
#d) selection sort

#a)
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
def insert(head, el):
    dummy=Node(-float('inf'))
    dummy.next=head
    head=dummy
    while head.next!=None and head.next.val<el.val:
        head=head.next
    el.next=head.next
    head.next=el
    return dummy.next
#b) cos tu nie gra
def insertion_sort(head):
    res=Node()
    while head!=None:
        tmp=head
        tmp.next=None
        head=head.next
        insert(res,tmp)
    head=res.next
#c)
def get_max(head):
    maxi=Node(-float('inf'))
    while head.next!=None:
        if head.next.val>maxi.val:
            maxi=head.next
            save=head
        head=head.next
    save.next=save.next.next
    maxi.next=None
    return maxi

L=create([4,5,7,3,9])
#wypisz(get_max(L))

#z.2
def minmax(T):
    minT=float('inf')
    maxT=-float('inf')
    N=len(T)
    for i in range (1,N):
        minT=min(minT,T[i])
        maxT=max(maxT,T[i])

def minmax_2(T): #O(3/2n) czemu?
    minT=maxT=T[-1]
    N=len(T)
    for i in range (1,N,2):
        if T[i]>T[i-1]:
            a,b=T[i],T[i-1]
        else:
            a,b=T[i-1],T[i]
        minT,maxT=min(minT,b),min(maxT,a)
    return minT,maxT

def selection_sort(L):
    dummy=Node()
    dummy.next=L
    L=dummy
    H=Node()
    while L.next != None:
        x=get_max(L) #tutaj z L usuwamy więc sie skraca
        x.next=H.next
        H.next=x
    L=H.next
    return L
wypisz(selection_sort(L))
#najmniejszy element równy key
def bin_search(T,key):
    left = 0
    right = len(T) - 1
    while left < right:
        mid = (left+right)//2
        if T[mid] == key:
            right = mid
        elif T[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return left
