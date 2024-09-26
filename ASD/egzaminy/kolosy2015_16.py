class Node:
    def __init__(self):
        self.val = None
        self.next = None
def sumSort(A):
    n = int((len(A))**(0.5))
    Sums = [None]*(len(A)//n)
    cnt = 0
    for i in range (n**2):
        cnt += A[i]
        if i%n + 1 == n:
            Sums[i//n] = cnt,i//n
            cnt = 0
    Sums = sorted(Sums)
    print(Sums)
    ans = [None]*(len(A))
    j = 0
    for sum in Sums:
        for i in range (n*sum[1],n*sum[1] + n):
            print(n*sum[1],n*sum[1] + n,j)
            ans[j] = A[i]
            j += 1
    return ans

#print(sumSort([5,4,3,6,5,3,5,6,7,4,5,6,7,3,2,5,7,4,2,5,16,13,2,8,0]))

def create(T):  #dokładanie od tyłu
    head=Node()
    dummy=head
    for el in T:
        head.next=Node()
        head.next.val = el
        head=head.next
    return dummy.next
def wypisz(first):
    while first!=None:
        print(first.val,end=' ')
        first=first.next
    print("")
def insert(p,tmp):
    dummy = Node()
    dummy.next = p
    p = dummy
    while p.next != None and p.next.val < tmp.val:
        p = p.next
    tmp.next = p.next
    p.next = tmp
    return dummy.next
def fixSortedList(p):
    start = p
    if p.val > p.next.val:
        tmp = p
        p = p.next
        tmp.next = None
        return insert(p,tmp)
    if p.next.next == None:
        return start
    left = p
    p = p.next
    right = p.next
    while right != None:
        print(left.val,p.val,right.val,)
        if (p.val < left.val and p.val < right.val and left.val <= right.val) or (p.val > left.val and p.val > right.val and left.val <= right.val):
            left.next = right
            tmp = p
            left,p,right = left.next, p.next, right.next
            tmp.next = None
            return insert(start,tmp)
        left,p,right = left.next, p.next, right.next
    if left.val > p.val:
        left.next = None
        return insert(start,p)
    return start

import random
def generate_sorted_array_with_change(size, change_index):
    arr = [random.randint(1, 100) for _ in range(size)]  # Generowanie losowej tablicy
    arr.sort()  # Sortowanie tablicy
    new_value = random.randint(1, 100)  # Losowa wartość dla zmiany
    arr[change_index] = new_value  # Zmiana wartości w określonym indeksie
    return arr
p = create(generate_sorted_array_with_change(3,random.randint(0,2)))
wypisz(fixSortedList(p))