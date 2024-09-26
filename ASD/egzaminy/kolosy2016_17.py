#bucket sort na linked listach w przedziale 0-10
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
def length(p):
    cnt = 0
    while p != None:
        p = p.next
        cnt += 1
    return cnt - 1

def insert(p,key):
    while p.next != None and key.val > p.next.val:
        p = p.next
    key.next = p.next
    p.next = key

def end(p):
    while p.next != None:
        p = p.next
    return p

def bucket_sort(p):
    N = length(p)
    buckets = [Node() for i in range (N+1)]   
    p = p.next
    while p != None:
        tmp = p
        p = p.next
        tmp.next = None
        insert(buckets[int((tmp.val/10))*N],tmp)
    i = 0
    while buckets[i].next == None:
        i += 1
    start = buckets[i]
    end_prev = end(buckets[i]) #koniec poprzedniego kubełka
    i += 1
    while i < N+1:
        if buckets[i].next != None:
            end_prev.next = buckets[i].next 
            end_prev = end(buckets[i])
        i += 1
    return start.next

p = create([None,9,6,4])
wypisz(bucket_sort(p)) #chyba jak jest otwarty w 10 to mozna zrobic N kubelkow ale tak tez ok