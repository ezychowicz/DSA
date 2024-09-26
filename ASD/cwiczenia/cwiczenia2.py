# #liczba inwersji w tablicy
# class Node():
#     def __init__(self,val):
#         self.next = None
#         self.val = val
# def zad(T):
#     cnt=0
#     def merge_cnt(T,p,q,r):
#         nonlocal cnt
#         L=[T[p+i] for i in range(q-p+1)]
#         R=[T[q+j] for j in range (1,r-q+1)]
#         L.append(float('inf'))
#         R.append(float('inf'))
#         i,j,k=0,0,0
#         L_len=q-p+1
#         while L[i]!=float('inf') or R[j]!=float('inf'):
#             if L[i]<=R[j]:
#                 T[p+k]=L[i]
#                 i+=1
#             else:
#                 print(L[i],R[j],L_len-i,cnt)
#                 T[p+k]=R[j]
#                 j+=1
#                 cnt+=L_len-i
#             k+=1

#     def mergesort(T,p,r):
#         nonlocal cnt
#         if p==r:
#             return 0 
#         q=(p+r)//2
#         mergesort(T,p,q)
#         mergesort(T,q+1,r)
#         merge_cnt(T,p,q,r)
        
#     mergesort(T,0,len(T)-1)
#     print(T)
#     return cnt

# #print(zad(T = [8,4,2,1]))

# #mergesort bez nonlocala
# # def mergesort(T,p,r):
# #     cnt=0
# #     if p==r:
# #         return 0 
# #     q=(p+r)//2
# #     cnt+=mergesort(T,p,q)
# #     cnt+=mergesort(T,q+1,r) #w konkretnym rozkladzie suma inwersji to suma inwersji z podrozkladow i inwersje wychodzace ze scalania
# #     cnt+=merge_cnt(T,p,q,r)
# #     return cnt





# #2sum
# def twoSum(T,x):
#     N=len(T)
#     i,j=0,N-1
#     while i!=j:
#         if T[i]+T[j]==x:
#             return True,i,j
#         if T[i]+T[j]<x:
#             i+=1
#         else:
#             j-=1
#     return False
# # print(twoSum([1,4,5,6,7,34,564],39))








# #pojemniki z wodą
# def val(A):
#     if A[2]==0:
#         return A[0][1]
#     return A[1][1]

# def merge(T,p,q,r):
#     L=[T[p+i] for i in range (q-p+1)]
#     R=[T[q+i] for i in range (1,r-q+1)]
#     L.append(((0,float('inf')),0,0))
#     R.append(((0,float('inf')),0,0))
#     i,j,k=0,0,0
#     while val(L[i])!=float('inf') or val(R[j])!=float('inf'):
#         if val(L[i])>val(R[j]):
#             T[p+k]=R[j]
#             j+=1
#         else:
#             T[p+k]=L[i]
#             i+=1
#         k+=1

# def mergesort(T,p,r):
#     if r==p:
#         return 
#     q=(p+r)//2
#     mergesort(T,p,q)
#     mergesort(T,q+1,r)
#     merge(T,p,q,r)
    
# def convert(T,T_length):
#     #start=0,end=1, zakładam: w inpucie: (wspł.prawy dolny, wspł.lewy górny)
#     N=T_length
#     new=[None]*(2*N)
#     j=0
#     for i in range (N):
#         new[j]=(T[i][0],T[i][1],0)
#         j+=1
#         new[j]=(T[i][0],T[i][1],1)
#         j+=1
#     return new

# def surface(A,B): #podstawa pojemnika o przekatnych wspolrzednych A, B
#     return abs(A[0]-B[0])

# def pouring(T,A):
#     if len(T)==0:
#         return 0
#     N=len(T)
#     T=convert(T,N)
#     mergesort(T,0,2*N-1)
#     print("sorted:",T)
#     i=1
#     cnt=0
#     prev=val(T[0])
#     S=surface(T[0][0],T[0][1])
#     while A>=0 and i<2*N:
#         curr=val(T[i])
#         A-=S*(curr-prev)
#         prev=curr
#         if A<0:
#             break
#         if T[i][2]==0:
#             S+=surface(T[i][0],T[i][1])
#             print(surface(T[i][0],T[i][1]),T[i][0],T[i][1],S,i)
#         else:
#             S-=surface(T[i][0],T[i][1])
#             cnt+=1
#             print(surface(T[i][0],T[i][1]),T[i][0],T[i][1],S,i,cnt)
#         i+=1
#     return cnt 

# T=[[(1,0),(0,2)],[(1,3),(0,7)],[(2,4),(1,5)],[(4,5),(2,6)],[(3,0),(1,1)]]
# #print(pouring(T,9))








# #lider
# import math
# def lider(T):
#     N = len(T)
#     cnt = 0
#     curr = None
#     for i in range (N):
#         if cnt == 0:
#             curr = T[i]
#             cnt = 1
#         else:
#             if T[i] == curr:
#                 cnt += 1
#             else:
#                 cnt -= 1
#     if cnt == 0:
#         return False
#     cnt = 0
#     for i in range (N):
#         if T[i] == curr:
#             cnt += 1
#     if cnt >= math.ceil(N/2):
#         return True
#     return False
# # T=[1,2,3,3,9,9,9,9,9,9,9,9,9,9,93,9,2,1,9,7,9,4,3,1,9,1,1]
# # print(lider(T),len(T))






# def merge2(T1,T2,N):
#     T = [None]*N
#     T1.append(float('inf'))
#     T2.append(float('inf'))
#     i,j,k=0,0,0
#     while T1[i] != float('inf') or T2[j] != float('inf'):
#         if T1[i] <= T2[j]:
#             T[k] = T1[i]
#             i += 1
#         else:
#             T[k] = T2[j]
#             j += 1
#         k += 1
#     return T
# def mergesort2(T):
#     N = len(T)
#     if N<=1:
#         return T
#     mid = len(T)//2
#     T1 = T[0:mid]
#     T2 = T[mid:N]
#     T1 = mergesort2(T1)
#     T2 = mergesort2(T2)
#     return merge2(T1,T2,N)







# #binary search
# def bs(T, x, left, right):
#     print(T[left:right+1])
#     if right - left <= 1: #gdy =1 to nieciekawa sytuacja bo sie zakopujemy
#         if T[left] == x:
#             return left
#         if T[right] ==x:
#             return right
#         else:
#             return -1
#     mid = (left + right)//2
#     if T[mid] < x:
#         return bs(T, x, mid, right)
#     elif T[mid] == x:
#         return mid
#     else:
#         return bs(T, x, left, mid)
# print(bs([1,3,6,8,9,12,14,34,45,456],1,0,len([1,3,6,8,9,12,14,34,45,456])-1))




#POCZĄTEK ZAJĘĆ


# #mergesort na seriach naturalnych
class Node:
    def __init__(self,val = None, next = None):
        self.val = val
        self.next = next


# #a)scalanie
# def merge(p1,p2):  
#     res = head = Node()
#     while p1 != None and p2 != None:
#         if p1.val<p2.val:
#             head.next = p1
#             p1 = p1.next
#         else:
#             head.next = p2
#             p2 = p2.next
#         head = head.next
#     if p1 != None:
#         head.next = p1
#         head = head.next
#     if p2 != None:
#         head.next = p2
#         head = head.next
#     return res.next

# #c)znalezienie konca listy
# def end(p):
#     while p.next != None:
#         p = p.next
#     return p

# #b)wyciaganie serii naturalnych
# def exctract(dummy):
#     p = dummy.next
#     start = p
#     while p.next != None and p.val <= p.next.val:
#         p = p.next
#     dummy.next = p.next
#     p.next = None
#     return start
# #d)mergesort
# def mergesort(p):
#     dummy = Node()
#     dummy.next = p
#     last = end(dummy)
#     while True:
#         exc1 = exctract(dummy)
#         if dummy.next != None:
#             exc2 = exctract(dummy)
#         else:
#             dummy.next = exc1
#             return dummy.next
#         merged = merge(exc1,exc2)
#         if dummy.next == None:
#             return merged
#         last.next = merged
#         last = end(last)

# def create(T):  #dokładanie od tyłu
#     head=Node()
#     dummy=head
#     for el in T:
#         head.next=Node(el)
#         head=head.next
#     return dummy.next
# def wypisz(first):
#     while first!=None:
#         print(first.val,end=' ')
#         first=first.next
#     print("")

# p = create([1,2,3,1])

# wypisz(mergesort(p))









#największy przedział (w relacji inkluzji)
#f(ai) - liczba przedzialow zaczynajacych sie przed ai
#g(bi) - liczba przedziałów kończących się przed bi
#odp: g(ai) - f(bi) zad. rozważyć gdy sie zawierajają niewłaściwie

#po posortowaniu da sie juz liniowo

# def merge(T1,T2):
#     T = [None]*(len(T1)+len(T2))
#     T1.append([float('inf'),None])
#     T2.append([float('inf'),None])
#     i,j,k = 0,0,0
#     while T1[i][0] != float('inf') or T2[j][0] != float('inf'):
#         if T1[i][0] > T2[j][0]:
#             T[k] = T2[j]
#             j += 1
#         else:
#             T[k] = T1[i]
#             i += 1
#         k += 1
#     return T

# def mergesort(T):
#     if len(T) <= 1:
#         return T
#     mid = len(T)//2
#     T1 = T[:mid]
#     T2 = T[mid:]
#     T1 = mergesort(T1)
#     T2 = mergesort(T2)
#     return merge(T1,T2)


# def convert(T):
#     T = mergesort(T)
#     i = 0
#     for el in T:
#         el.append(i)
#         i += 1
#     return T

# def merge2(T1,T2):
#     T = [None]*(len(T1)+len(T2))
#     T1.append([None,float('inf')])
#     T2.append([None,float('inf')])
#     i,j,k = 0,0,0
#     while T1[i][1] != float('inf') or T2[j][1] != float('inf'):
#         if T1[i][1] > T2[j][1]:
#             T[k] = T2[j]
#             j += 1
#         else:
#             T[k] = T1[i]
#             i += 1
#         k += 1
#     return T

# def mergesort2(T):
#     if len(T) <= 1:
#         return T
#     mid = len(T)//2
#     T1 = T[:mid]
#     T2 = T[mid:]
#     T1 = mergesort2(T1)
#     T2 = mergesort2(T2)
#     return merge2(T1,T2)

# def przedzialy(T):
#     T = convert(T)
#     T = mergesort2(T)
#     print(T)
#     maxi = -float('inf')
#     for i in range (len(T)):
#         if i - T[i][2] > maxi:
#             maxi = i - T[i][2]
#             save = T[i]
#     return save,maxi
# T = [[-0.5, 2], [12, 18],[0, 8],[15, 16.5],[11, 17], [15.5, 18.5], [-1, 6], [13, 14],[1, 1.5],[4, 8.5], [6, 7],]
# print(przedzialy(T))


# class Node:
#     def __init__(self):
#         self.val = None
#         self.next = None
# def create(T):  #dokładanie od tyłu
#     head=Node()
#     dummy=head
#     for el in T:
#         head.next=Node()
#         head.next.val = el
#         head=head.next
#     return dummy.next

# def wypisz(first):
#     while first!=None:
#         print(first.val,end=' ')
#         first=first.next
#     print("")

# def exc_sub(p):
#     dummy = Node()
#     dummy.next = p
#     dummy.val = -float('inf')
#     p = dummy
#     while p.next != None and p.next.val >= p.val:
#         p = p.next
#     after_del = p.next
#     p.next = None
#     return dummy.next,after_del

# def merge(p1,p2):
#     start = merged = Node()
#     while p1 != None and p2 != None:
#         if p1.val <= p2.val:
#             merged.next = p1
#             p1 = p1.next
#         else:
#             merged.next = p2
#             p2 = p2.next
#         merged = merged.next
#     if p1 != None:
#         merged.next = p1
#     elif p2 != None:
#         merged.next = p2
#     return start.next

# def end(p):
#     while p.next != None:
#         p = p.next
#     return p
# def mergesort_naturalseries(p):
#     right = p
#     while True:
#         x = exc_sub(right)
#         left1 = x[0]
#         wypisz(left1)
#         right = x[1]
#         wypisz(right)
#         if right == None:
#             print("a")
#             return left1
#         x = exc_sub(right)
#         left2 = x[0]
#         right = x[1]
#         if right == None:
#             return merge(left1,left2)
#         last = end(right)
#         last.next = merge(left1,left2)
#         wypisz(right)

# wypisz(mergesort_naturalseries(create([1,2,3,4,4,1,5,7,4,5,6,1,7,4])))