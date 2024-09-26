class Node:
    def __init__(self):
        self.val = None
        self.next = None
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
#quicker_sort on linked list
def partition(p):
    x = end(p)
    left_start = left = Node()
    right_start = right = Node()
    mid_start = mid = Node()
    while p != None:
        if p.val < x.val:
            left.next = p
            left = left.next
        elif p.val > x.val:
            right.next = p
            right = right.next
        else:
            mid.next = p
            mid = mid.next
        p = p.next
    left.next = None
    right.next = None
    mid.next = None
    return left_start.next,right_start.next,mid_start.next
def end(p):
    while p.next != None:
        p = p.next
    return p
def quicker_sort(p):
    if p == None or p.next == None:
        return p
    q = partition(p)
    p_left = q[0]
    p_right = q[1]
    mid = q[2]
    p_left = quicker_sort(p_left)
    p_right = quicker_sort(p_right)
    if p_left == None:
        mid.next = p_right
        return mid    
    else:
        left_end = end(p_left)
        left_end.next = mid
        mid.next = p_right
        return p_left
    
p = create([4,2,3,7,8,6,4,5,0,1])

wypisz(quicker_sort(p))


def possible(u,v,w):
    count = [0]*(ord('z') - ord('a') + 1)
    for i in range (len(w)):
        count[ord(w[i]) - ord('a')] = 0
    for i in range (len(u)):
        count[ord(u[i]) - ord('a')] += 1
    for i in range (len(v)):
        count[ord(v[i]) - ord('a')] += 1
    for i in range (len(w)):
        count[ord(w[i]) - ord('a')] -= 1
        if count[ord(w[i]) - ord('a')] < 0:
            return False
    return True

print(possible("abcd","efuz","ebzx"))