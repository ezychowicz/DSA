class Node:
    def __init__(self,val = None,next = None):
        self.val = val
        self.next = next

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
#stack - linked list
def push(p,val):
    new = Node(val)
    new.next = p
    p = new
    return p
def pop(p):
    tmp = p
    p = p.next
    tmp.next = None
    return p,tmp

#queue - array
'''
size = 0
q_i = 0
q_j = 0

def create_queue(max_size):
    global size
    q = [None]*max_size
    size = max_size
    return q
def push(q,val):
    global q_i,q_j,size
    q_j = (q_j+1)%size
    q[q_j] = val

def pop(q):
    global q_i,q_j,size
    tmp = q[q_i]
    q[q_i] = None
    q_i = (q_i+1)%size
    return tmp
'''
#queue - linked list
'''
def push(head,tail,val):
    if head == None:
        head = Node(val)
        tail = head
    else:
        tail.next = Node(val)
        tail = tail.next
    return head,tail
                                     
def pop(head):
    tmp = head
    head = head.next
    tmp.next = None                            
    return tmp,head

head = None
tail = head                        
head,tail = push(head,tail,4)
head,tail = push(head,tail,3)
head,tail = push(head,tail,1)
head,tail = push(head,tail,2)
removed,head = pop(head)
removed,head = pop(head)
removed,head = pop(head)

wypisz(head)
'''

#doubly linked list
class DNode:
    def __init__(self,val = None,next = None,prev = None):
        self.val = val
        self.next = next
        self.prev = prev

def insert(p,key):
    start = p
    if p == None:
        return DNode(key)
    if p.val >= key:
        new = DNode()
        new.val,new.next = key,p
        p.prev = new
        p = new
        return p

    while p.next != None and p.next.val < key:
        p = p.next
    if p.next == None:
        new = DNode(key)
        new.prev = p
        p.next = new
        return start
    new = DNode(key)
    new.next = p.next
    new.prev = p
    p.next = new
    p.next.prev = new
    return start


def D_create(T):
    start = p = DNode()
    for el in T:
        p.next = DNode(el,None,p)
        p = p.next
    return start.next

def D_wypisz(p):
    while p != None:
        print(p.val,end =' ')
        p = p.next
    print("")
p = None
p = insert(p,4)
p = insert(p,3)
p = insert(p,3.5)
D_wypisz(p)

