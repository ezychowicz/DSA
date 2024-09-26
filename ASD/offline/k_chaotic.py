#Emil Żychowicz
# Algorytm składa się z dwóch różnych algorytmów, które uruchamiane są w zależności od wejściowego k. 
# Dla k>=10: Algorytm opiera się na przechodzeniu przez listę o k elementów za każdym razem sortując fragmetny listy o długości 2*k elementów. 
# W ten sposób wszystkie elementy mają okazję przy sortowaniu trafić na właściwe miejsce. Fragmenty o długości 2*k są wyciągane z listy,
# sortowane algorytmem mergesort,a następnie z powrotem dołączane do głównej listy. Zł. czasowa: O(nlogk)
# Dla k<10: Algorytm przechodzi przez listę i za każdym razem wyszukuje minimum w k+1 elementowej liście. Wyciąga je i ustawia 
# przed sprawdzany aktualnie k+1 elementowy podciąg. Podciąg przesuwamy za każdym razem o 1. W ten sposób również każdy element 
# ma możliwość przeniesienia się o k elementów w odpowiednią stronę. Zł. czasowa: O(nk)
# dla k = theta(1): theta(n)
# dla k = theta(logn): theta(nlog(logn))
# dla k = theta(n): theta(nlogn)
#from zad1testy import Node, runtests
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


def exctract(prev, end):
    to_exctract = prev.next
    to_save = end.next
    end.next = None
    return to_exctract, to_save 

def split(start): 
    fast = slow = start
    while fast.next != None and fast.next.next != None:
        fast,slow = fast.next.next,slow.next
    right = slow.next
    slow.next = None
    return right

def merge(p1,p2):  
    res = head = Node()
    while p1 != None and p2 != None:
        if p1.val<p2.val:
            head.next = p1
            p1 = p1.next
        else:
            head.next = p2
            p2 = p2.next
        head = head.next
    if p1 != None:
        head.next = p1
    if p2 != None:
        head.next = p2
    return res.next

def mergesort(start):
    if start == None or start.next == None:
        return start
    mid = split(start)
    start = mergesort(start)
    mid = mergesort(mid)
    return merge(start, mid)

def find_new_end(start,k):
    for i in range (2*k-1):
        start = start.next
    return start

def exctract_min(p,k): 
    save = p
    i = 0
    mini = float('inf')
    while p.next != None and i <= k:
        if p.next.val < mini:
            mini = p.next.val
            min_node = p.next
            min_next = p.next.next
            prev = p
        p = p.next
        i += 1
    prev.next = min_next
    after_del = save.next 
    return min_node, after_del

def SortH(p,k):
    if k >= 10:
        dummy = Node()
        dummy.next = p
        prev = dummy 
        start = p
        end = start
        i,j = 0,0
        while end.next != None and i < 2*k-1:
            end = end.next
            i += 1
        while end.next != None:
            exc = exctract(prev,end)
            sorted = mergesort(exc[0])
            prev.next = sorted
            start = sorted
            end = find_new_end(start,k)
            end.next = exc[1]
            j = 0
            while end.next != None and j < k:
                start, end, prev = start.next, end.next, prev.next
                j += 1
        exc = exctract(prev,end)
        sorted = mergesort(exc[0])
        prev.next = sorted
        return dummy.next
    else:
        dummy = Node()
        dummy.next = p
        p = dummy
        while p.next.next != None:
            exc = exctract_min(p,k)
            p.next = exc[0]
            exc[0].next = exc[1]
            p = p.next
        return dummy.next


#runtests( SortH, all_tests = True )