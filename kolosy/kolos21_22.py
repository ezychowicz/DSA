#1a
#z.1
# import math
# def dlg(K):
#     return math.floor(math.log(K,10))+1
# def prime(K):
#     i=3
#     if K==2:
#         return True
#     if K%2==0:
#         return False
#     if K<2:
#         return False
#     while i<=K**(0.5):
#         if K%i==0:
#             return False
#         i+=2
#     return True
# def rozne_cyfry(K):
#     digits=[False]*10
#     while K>0:
#         if digits[K%10]==False:
#             digits[K%10]=True
#         else:
#             return False
#         K//=10
#     return True
# def cutter(K):
#     n=dlg(K)
#     K_c=K
#     maxi=0
#     for M in range (n):
#         K_c=K
#         K_c=K_c%10**(n-M)
#         while K_c>0:
#             if prime(K_c) and rozne_cyfry(K_c):
#                 maxi=max(maxi,K_c)
#                 break
#             K_c//=10
#     return maxi
# from time import time

# def ciecie(K):
#     maxi=0
#     len=dlg(K)
#     for N in range (len):
#         a=K
#         a//=10**(N)
#         for j in range (len-N,1,-1):
#             if prime(a%10**(j)) and rozne_cyfry(a%10**(j)):
#                 maxi=max(maxi,a%10**(j))
#     return maxi
# print(cutter(1202742516874635683))
# print(ciecie(1202742516874635683))        
#z.2
# def convert(a):
#     digits=[False]*4
#     while a>0:
#         digits[a%4]=True
#         a//=4
#     return digits
# def check(b,digits):
#     while b>0:
#         if digits[b%4]==False:
#             return False
#         b//=4
#     return True
# def zad_2(T):
#     N=len(T)
#     cnt=1
#     maxi=1
#     for i in range (len(T)):
#         T[i]=convert(T[i])
#     print(T)
#     for start in range (N-1):
#         cnt=1
#         for i in range (start+1,N):
#             if T[start]==T[i]:
#                 cnt+=1
#         maxi=max(cnt,maxi)
#         print(cnt,T[start])
#     return maxi
                
# print(zad_2([546,53,643,13,46,4,4643,646,53,43,6436,45,674,213,5764,5,6,45,855,7,45,6,4,562,426,464,564]))

#1b
#z.1
# def zad_1(T):
#     N=len(T)
#     iloczyn=1
#     maxi=None
#     for i in range (N):
#         if T[i]==iloczyn and T[i]!=1:
#             maxi=T[i]
#         if prime(T[i]):
#             iloczyn*=T[i]
#     return maxi
# print(zad_1([18,2,18,2,18,18,18,4,18,3,18,12,18,5,18,7,18,18,18,18,18,18,18,18,18,18,11]))

#z.2
# def convert(a,b):
#     iloczyn=1
#     while a>0:
#         iloczyn*=a%b
#         a//=b
#     return prime(iloczyn)
# def permute3(N):
#     if N==0:
#         yield [0]
#         return
#     else:
#         for perm in permute3(N-1):
#             for k in range (N+1):
#                 yield perm[:k]+[N]+perm[k:]
#     return
# import math
# def dlg(a):
#     return math.floor(math.log(a,10))+1
# def zad_2(N):
#     T=list(str(N))
#     k=dlg(N)
#     for el in permute3(k-1):
#         num=0
#         for i in range (k):
#             #print(el[i])
#             num+=int(T[el[i]])*10**(i)
#         for b in range (2,16):
#             if convert(num,b):
#                 return b
#     return None
# print(zad_2(13))

#gr.b
#z.2
# from time import time
# start=time()
# def warunek(a,p):
#     primes=[2,3,5,7,11,13]
#     digits=[False]*p
#     while a>0:
#         if a%p!=1 and a%p not in primes:
#             return False
#         elif a%p!=1:
#             if digits[a%p]==False:
#                 digits[a%p]=True
#             else:
#                 return False
#         a//=p
#     return True if True in digits else False
# end=time()
# print(end-start)
# print(warunek(1554643634563457357567354564,4))
# def iloczyn(a,p):
#     il=1
#     while a>0:
#         il*=a%p
#         if a%p==0:
#             return False
#         a//=p
#     return True if prime(il) else False

# def prime(a):
#     if a<2:
#         return False
#     if a==2:
#         return True
#     if a%2==0:
#         return False
#     i=3
#     while i<=a**(0.5):
#         if a%i==0:
#             return False
#         i+=2
#     return True
# start=time()
# print(iloczyn(1554643634563457357567354564,4))
# end=time()
# print(end-start)

#poprawkowy
#z.1
# def counter(T,N,to_check):
#     N_T=len(T)
#     res=[[0 for _ in range (N)] for _ in range (N)]
#     for i in range (N_T):
#         for el in to_check:
#             if 0<=T[i][0]+el[0]<N and 0<=T[i][1]+el[1]<N:
#                 res[T[i][0]+el[0]][T[i][1]+el[1]]+=1
#     return res
# def usun(T,N):
#     maxi=0
#     to_check=[(2,-1),(2,1),(-2,-1),(-2,1),(1,2),(1,-2),(-1,2),(-1,-2),(0,0)]
#     count_tab=counter(T,N,to_check)
#     print(*count_tab,sep='\n')
#     for skoczek in T:
#         cnt=0
#         for el in to_check:
#             if 0<=skoczek[0]+el[0]<N and 0<=skoczek[1]+el[1]<N:
#                 if count_tab[skoczek[0]+el[0]][skoczek[1]+el[1]]==1:
#                     cnt+=1
#         maxi=max(cnt,maxi)
#     return maxi
# print(usun( [(1, 0), (2, 3), (4, 1), (4, 5)],8))

#z.3
# import random
# def zad3(T):
#     N=len(T)
#     def nwd(a,b):
#         while b>0:
#             a,b=b,a%b
#         return a==1
#     def f(i,j,goal):
#         if (i,j)==goal:
#             return 0
#         mini=float('inf')
#         for k in range (i+1,N):
#             if nwd(T[i][j],T[k][j]):
#                 mini=min(mini,f(k,j,goal))
#         if goal!=(N-1,0):
#             for k in range (j+1,N):
#                 if nwd(T[i][j],T[i][k]):
#                     mini=min(mini,f(i,k,goal))
#         else:
#             for k in range (j):
#                 if nwd(T[i][j],T[i][k]):
#                     mini=min(mini,f(i,k,goal))
#         return 1+mini
#     wieza1=f(0,0,(N-1,N-1))
#     wieza2=f(0,N-1,(N-1,0))
#     print(wieza1,wieza2)
#     if wieza1>wieza2:
#         return 1
#     if wieza2>wieza1:
#         return 2
#     return 0 #gdy oba są float('inf') albo są równe
# print(zad3([[random.randint(1,100) for _ in range (8)] for _ in range (8)]))

#poprawkowy
#trojki z.1
# def nwd(a,b):
#     while b>0:
#         a,b=b,a%b
#     return a
# def nwd_3(a,b,c):
#     return nwd(nwd(a,b),c)
# def trojki(T):
#     cnt=0
#     N=len(T)
#     M=N**2
#     for i in range (M-2*N):
#         w1,k1=i//N,i%N
#         for j in range ((w1+1)*N,M-N):
#             w2,k2=j//N,j%N
#             if k2==k1:
#                 continue
#             for k in range ((w2+1)*N,M):
#                 w3,k3=k//N,k%N
#                 if k3==k2 or k3==k1:
#                     continue
#                 if nwd_3(T[w1][k1],T[w2][k2],T[w3][k3])==1:
#                     cnt+=1
#     return cnt
# import random
# print(trojki(T=[[random.randint(1,100) for _ in range (15)] for _ in range (15)]))

#z.2 poprawkowy (sztabki)
def zad(N,T):
    def is_prime(a):
        if a<2:
            return False
        if a==2:
            return True
        if a%2==0:
            return False
        i=3
        while i<=a**(0.5):
            if a%i==0:
                return False
            i+=2
        return True
    path=[0]*N
    def f(sztabki,p,path):
        print(path)
        if p==N and sztabki==0:
            print(path)
            return True
        if p==N:
            return False
        for i in range (sztabki+1):
            path[p]=T[p]+i
            if is_prime(T[p]+i) and f(sztabki-i,p+1,path):
                return True
            path[p]=0
        i=0
        sztabki+=1
        while sztabki<=6:
            i+=1
            if T[p]-i<=1:
                break
            path[p]=T[p]-i
            if is_prime(T[p]-i) and f(sztabki,p+1,path):
                return True
            sztabki+=1
            path[p]=0
        return False 
    return f(0,0,path)
print(zad(3,T = [10, 20, 35]))