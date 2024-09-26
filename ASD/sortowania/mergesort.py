def merge(T1,T2):
    T = [None]*(len(T1) + len(T2))
    T1.append(float('inf'))
    T2.append(float('inf'))
    i,j,k = 0,0,0
    while T1[i] != float('inf') or T2[j] != float('inf'):
        if T1[i] <= T2[j]:
            T[k] = T1[i]
            i += 1
        else:
            T[k] = T2[j]
            j += 1
        k += 1
    return T

def mergesort(T):
    if len(T) == 1:
        return T
    mid = len(T)//2
    T1 = mergesort(T[:mid])
    T2 = mergesort(T[mid:])
    return merge(T1,T2)


#LINKED LIST
class Node:
    def __init__(self):
        self.val = None
        self.next = None

def create(T):  
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

def middle(p):
    slow, fast = p,p
    while fast.next != None and fast.next.next != None:
        slow,fast = slow.next, fast.next.next
    return slow

def merge(p1,p2):
    start = p = Node()
    while p1 != None and p2 != None:
        if p1.val <= p2.val:
            p.next = p1
            p1 = p1.next
        else:
            p.next = p2
            p2 = p2.next
        p = p.next
    if p1 != None:
        p.next = p1
    else:
        p.next = p2
    return start.next

def mergesort(p):
    if p == None or p.next == None:
        return p
    mid = middle(p)
    left = p
    right = mid.next
    mid.next = None
    left = mergesort(left)
    right = mergesort(right)
    return merge(left,right) 


# def merge(T,p,q,r):
#     L=[T[p+i] for i in range (q-p+1)]
#     L.append(float('inf'))
#     R=[T[q+i] for i in range (1,r-q+1)]
#     R.append(float('inf'))
#     i,j,k=0,0,0
#     while L[i]!=float('inf') or R[j]!=float('inf'):
#         if L[i]>R[j]:
#             T[p+k]=R[j]
#             j+=1
#         else:
#             T[p+k]=L[i]
#             i+=1
#         k+=1

# def mergesort(T,p,r):
#     if p>=r:
#         return 
#     q=(r+p)//2
#     mergesort(T,p,q)
#     mergesort(T,q+1,r)
#     merge(T,p,q,r)

# #wiecej pamieci, bardziej czytelne


# T = [6,8,3,2,8,4,8,4,6,7,9,3,1,23,6,87,34,3]
# T = mergesort(T)
# print(T)

#linked listy




import random
p = create([random.randint(1,100) for i in range (10)])
p = mergesort(p)
wypisz(p)




