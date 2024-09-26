# def find(k):
#     a=1
#     b=2
#     count=0
#     min_count=float('inf')
#     min_distance=float('inf')
#     s=str() 
#     while a<=k or b<=k:
#         count+=1
#         if abs(a-k)<min_distance: #automatycznie bierze pod uwage wyraz o mniejszym numerze bo bedzie on wczesniej, a nierownosc jest silna wiec nie zmieni sie gdy napotka jtaki sam min_distance
#             min_distance=abs(a-k)
#             min_count=count
#             s="a"
#         if abs(b-k)<min_distance:
#             min_distance=abs(b-k)
#             min_count=count
#             s="b"
#         b=a+b
#         a=a+b/3
#     count+=1
#     if abs(a-k)<min_distance:
#         min_distance=abs(a-k)
#         min_count=count
#         s="a"
#     if abs(b-k)<min_distance:
#         min_distance=abs(b-k)
#         min_count=count
#         s="b"
#     return min_count,s
# print(find(50))
# import random
# MAX=10000000
# T=[random.randint(1,1000) for i in range (MAX)]
# def the_largest(T):
#     tab=[]
#     for j in range (10):
#         tab.append(T[j])
#     tab.sort(reverse=True)
#     for i in range (10,len(T)):
#         if T[i]>tab[-1]:
#             j=0
#             while T[i]<tab[j]:
#                 j+=1
#             tab.insert(j,T[i])
#             tab.pop()
#     return sum(tab)
# print(the_largest(T))

#gr 2:
# k=int(input("liczba:"))
# a,b,fib_1,fib_2,fib_3=1,1,1,1,1
# c=0
# i=0
# while i<k:
#     if c!=min(a,fib_1):
#         c=min(a,fib_1)
#         i+=1
#     if a>fib_1:
#         fib_1,fib_2,fib_3=fib_2,fib_3,fib_1+fib_2+fib_3
#     elif a<fib_1:
#         a,b=b,a+b
#     else:
#         a,b=b,a+b
#         fib_1,fib_2,fib_3=fib_2,fib_3,fib_1+fib_2+fib_3
# print(c)
# import random
# max_c=-float('inf')
# count=0
# T=[2,9,3,1,7,11,9,6,7,7,1,3,9,12,15]
# for start in range (len(T)-1):
#     i=start
#     j=len(T)-1
#     while i<=len(T)-1 and j>=0:
#         if T[i]==T[j]:
#             j_d,i_d=j,i
#             while j_d>=0 and i_d<=len(T)-1 and T[j_d]==T[i_d]:
#                 j_d-=1
#                 i_d+=1
#                 count+=1
#             if count>max_c:
#                 max_c=count
#             count=0
#         j-=1
# print(max_c)

#kartkowka 2 gr.a 
#z.1
# def rows_cols(T):
#     N=len(T)
#     row=[0]*N
#     col=[0]*N
#     for i in range (N):
#         for j in range (N):
#             row[i]+=T[i][j]
#             col[j]+=T[i][j]
#     return row,col
# def suma(w1,k1,w2,k2,row,col,T):
#     res=0
#     if w1==w2:
#         res=row[w1]+col[k1]+col[k2]-2*(T[w1][k1]+T[w2][k2])
#     elif k1==k2:
#         res=row[w1]+row[w2]+col[k1]-2*(T[w1][k1]+T[w2][k2])
#     else:
#         res=row[w1]+row[w2]+col[k1]+col[k2]-2*(T[w1][k1]+T[w2][k2])-T[w1][k2]-T[w2][k1]
#     return res
# def zad(T,pos):
#     N=len(T)
#     w1,w2,k1,k2=pos[0][0],pos[1][0],pos[0][1],pos[1][1]
#     row,col=rows_cols(T)
#     curr_sum=suma(w1,k1,w2,k2,row,col,T)
#     for i in range (N):
#         if (i!=w1 and suma(i,k1,w2,k2,row,col,T)>curr_sum) or (i!=w2 and suma(w1,k1,i,k2,row,col,T)>curr_sum):
#             return True
#         if (i!=k1 and suma(w1,i,w2,k2,row,col,T)>curr_sum) or (i!=k2 and suma(w1,k1,w2,i,row,col,T)>curr_sum):
#             return True
#     return False
# board = [
#     [1, 1, 1],
#     [1, 1, 1],
#     [1, 1, 9]
# ]
# tower1 = (0, 0)
# tower2 = (2, 2)
# print(zad(board,[tower1,tower2]))


#kolokwium 2 z.1
# def nwd(a,b):
#     print(a,b)
#     if a==0 or b==0:
#         return 0
#     while b!=0:
#         a,b=b,a%b
#     return a
# import math
# def dlg(a):
#     return math.floor(math.log(a,10))+1
# def f(A,B,N):
#     print(A,B,N)
#     cnt=0
#     if N==0 and nwd(A,B)==1:
#         return 1
#     if N==0:
#         return 0
#     cnt+=f(10*A+N//10**(dlg(N)-1),B,N%10**(dlg(N)-1))+f(A,B*10+N//10**(dlg(N)-1),N%10**(dlg(N)-1))
#     return cnt
# print(f(0,0,21523))
def kolezanki(a,b):
    cnt=0
    digs=[False]*10
    while a>0:
        digs[a%10]=True
        a//=10
    while b>0:
        if digs[b%10]:
            cnt+=1
            if cnt>=2:
                return True
            digs[b%10]=False
        b//=10
    return False
def traverse(T):
    N=len(T)
    M=N**2
    v=[[False for _ in range (N)] for _ in range (N)]
    for i in range (M-1):
        for j in range (i+1,M):
            w1,k1,w2,k2=i//N,i%N,j//N,j%N
            if (v[w1][k1] and v[w2][k2]):
                continue
            if kolezanki(T[w1][k1],T[w2][k2]):
                v[w2][k2]=True
                v[w1][k1]=True
            if j==M-1 and not v[w1][k1]:
                T[w1][k1]=0
    if not v[N-1][N-1]: #ostatni element
        T[N-1][N-1]=0
    return T
import random
N=10
print(traverse([[random.randint(1,9) for _ in range (N)] for _ in range (N)]))


#z.2 poprawkowy

# def zad(T):
#     N=len(T)
#     moves=((1,2),(2,1),(1,-2),(2,-1))
#     def f(w,k):
#         if w==N-1:
#             return 0
#         mini=float('inf')
#         for el in moves:
#             if 0<=el[0]+w<N and 0<=el[1]+k<N and T[el[0]+w][el[1]+k]==False:
#                 mini=min(mini,f(el[0]+w,el[1]+k))
#         return 1+mini
#     mini_res=float('inf')
#     for k in range (N):
#         if T[0][k]==False:
#             mini_res=min(mini_res,f(0,k))
#     return mini_res if mini_res!=float('inf') else "brak"
# print(zad([
#  [True, False, True, False, True, False, True, False],
#     [False, True, False, True, False, True, False, True],
#     [True, False, True, False, True, False, True, False],
#     [False, True, False, True, False, True, False, True],
#     [True, False, True, False, True, False, True, False],
#     [False, True, False, True, False, True, False, True],
#     [True, False, True, False, True, False, True, False],
#     [False, True, False, True, False, True, False, True],
# ]))