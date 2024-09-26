# #poprawkowy
# #z.2
# def nwd(a,b):
#     while b!=0:
#         a,b=b,a%b
#     return a
# def nww(a,b):
#     return a*b//nwd(a,b)
# def nww_n(T):
#     N=len(T)
#     curr_nww=T[0]
#     for i in range (1,N):
#         curr_nww=nww(curr_nww,T[i])
#     return curr_nww
# def add_n(T):
#     N=len(T)
#     mian=[m for (l,m) in T]
#     dol=nww_n(mian)
#     gora=0
#     for i in range (N):
#         gora+=T[i][0]*dol//T[i][1]
#     if gora/dol==2022:
#         return True
#     return False
# from copy import deepcopy
# ans=[]
# def gen_comb(N,K,res):
#     global ans
#     if len(res)==K:
#         ans.append(deepcopy(res))
#         return 
#     else:
#         if res==[]:
#             i=0
#         else:
#             i=res[-1]+1
#         while i<N:
#             #res.append(i)
#             gen_comb(N,K,res+[i])
#             #res.pop()
#             i+=1
#     return ans
# def translate(T):
#     N=len(T)
#     for K in range (1,N):
#         to_sum=[0]*K
#         for el in gen_comb(N,K,[]):
#             i=0
#             for el_ in el:
#                 to_sum[i]=T[el_]
#                 i+=1
#             if add_n(to_sum):
#                 return True
#     return False
# print(translate())





#z.1
# def compare(T,start,k):
#     q=T[start]/T[start+k]
#     i=1
#     while i<k:
#         if T[start+i]/T[start+k+i]!=q:
#             return False
#         i+=1   
#     return True

# def sequence(T):
#     N=len(T)
#     for k in range (N//2,2,-1):
#         i=0
#         while i+2*k<N:
#             if compare(T,i,k):
#                 return i,i+k-1
#             i+=1
#     return "brak"

# print(sequence([2,5,7,3,2,3,5,7,6,9,15,21,17,19,23,2,6,4,8,3,5,7,1,3,2]))

#z.2
# def czy_podciag(n):
#     a,b=1,2
#     while a<n:
#         a,b=b,a+b-1
#     return a==n
# def traverse(T):
#     N=len(T)
#     for i in range (N-2):
#         j=0
#         k=2
#         cnt=2
#         while k+i<N:
#             if T[i+k][j+k]==T[i+k-1][j+k-1]+T[i+k-2][j+k-2]-1 and czy_podciag(T[i+k-2][j+k-2]):
#                 cnt+=1
#             k+=1
#         if cnt>=3:
#             return cnt
#     for i in range (1,N-2):
#         j=0
#         k=2
#         cnt=2
#         while k+i<N:
#             if T[j+k][i+k]==T[j+k-1][i+k-1]+T[j+k-2][i+k-2]-1 and czy_podciag(T[j+k-2][i+k-2]):
#                 cnt+=1
#             k+=1
#         if cnt>=3:
#             return cnt
# print(traverse([[4,5,14,78,3],[4,5,6,22,3],[4,5,6,35,35],[4,5,6,78,3],[4,5,6,78,3]]))
                
#gr B 
#z.2
# def czynniki(a):
#     i=2
#     cnt=0
#     flag=False
#     pierw=a**(0.5)
#     while a!=1 and i<=a**(0.5):
#         if a%i==0:
#             a//=i
#             if flag==False:
#                 cnt+=1
#                 if cnt>2:
#                     return False
#                 flag=True
#         else:
#             i+=1
#             flag=False
#     if a>1 and pierw%1==0 and cnt<=2:
#         return True
#     elif a>1 and pierw%1!=0:
#         if cnt+1>2:
#             return False 
#         else:
#             return True
#     return True if cnt<=2 else False

# def square():
#     T=generuj()
#     N=len(T)
#     for bok in range (2,N):
#         for i in range (N-bok+1):
#             for j in range (N-bok+1):
#                 if czynniki(T[i][j]*T[i+bok-1][j+bok-1]*T[i][j+bok-1]*T[i+bok-1][j]):
#                     return bok
#     return 0
# def generuj():
#     import random
#     T=[[random.randint(1,100) for _ in range (20)] for _ in range (20)]
#     return T
# print(square())


#z.3A
# def zad3(N,L):
#     def illegal(L):
#         v=[[False for _ in range (N)] for _ in range (N)]
#         for el in L:
#             v[el[0]][el[1]]=True
#         return v
#     v=illegal(L)
#     moves=((1,0),(-1,0),(0,1))
#     v[0][0]=True
#     def f(i,j,v):
#         if i==N-1 and j==N-1:
#             return 0
#         maxi=-float('inf')
#         for el in moves:
#             if 0<=el[0]+i<N and 0<=el[1]+j<N and not v[el[0]+i][el[1]+j]:
#                 v[el[0]+i][el[1]+j]=True #ten v pilnuje zeby w jednej sciezce nie wszedl na to samo (nie cofnął)
#                 maxi=max(maxi,f(el[0]+i,el[1]+j,v))
#                 v[el[0]+i][el[1]+j]=False
#         return 1+maxi
#     res=f(0,0,v)
#     return None if res==-float('inf') else res
# print(zad3(6,[(2, 1), (2, 3), (2, 5)]))

# #z.4A
# import random
# def zad4():
#     N=100
#     maxi=0
#     dist=0
#     moves=((2,1),(2,-1),(1,2),(1,-2),(-2,1),(-2,-1),(-1,2),(-1,-2))
#     T=[[random.randint(0,1) for _ in range (N)] for _ in range (N)]
#     print(T)
#     def d(pos1,pos2):
#         return max(abs(pos1[0]-pos2[0]),abs(pos1[1]-pos2[1]))
#     def convert(T):
#         for i in range (N):
#             for j in range (N):
#                 for el in moves:
#                     if 0<=el[0]+i<N and 0<=el[1]+j<N and T[el[0]+i][el[1]+j]!=1:
#                         T[el[0]+i][el[1]+j]=-1
#     convert(T)
#     print(T)
#     def place(T):
#         ans=None
#         maxi=-float('inf')
#         for i in range (N):
#             for j in range (N):
#                 if T[i][j]!=1:
#                     cnt=0
#                     for el in moves:
#                         if 0<=el[0]+i<N and 0<=el[1]+j<N:
#                             if T[el[0]+i][el[1]+j]==0:
#                                 cnt+=1
#                     if cnt>maxi:
#                         maxi=cnt
#                         dist=d((((N+1)//2),((N+1)//2)),(i,j))
#                         ans=(i,j)
#                     if cnt==maxi:
#                         if dist>d((((N+1)//2),((N+1)//2)),(i,j)):
#                             dist=d((((N+1)//2),((N+1)//2)),(i,j))
#                             ans=(i,j)
#         return ans
#     return place(T)
# print(zad4())


#z B3
# from copy import deepcopy
def rook(N,L):
    T=[[False for _ in range (N)] for _ in range (N)]    
    def convert(L,T):
        for el in L:
            T[el[0]][el[1]]=True
    convert(L,T)
    def f(w,k):
        if w==N-1 and k==N-1:
            return 0
        mini=float('inf')
        for i in range (k+1,N):
            if T[w][i]==True:
                break
            mini=min(mini,f(w,i))
        for j in range (w+1,N):
            if T[j][k]==True:
                break
            mini=min(mini,f(j,k))
        return 1+mini
    res=f(0,0)
    return res if res!=float('inf') else "nie da sie" 
print(rook(8,[(0,3),(1,7),(2,5),(3,3),(4,6),(5,2),(6,7),(7,4),(6,5)]))

#z pathem - konkatenacja   #CZY DA SIE UNIKNAC KONKATENACJI (JAK)
# from copy import deepcopy
# def rook(N,L):
#     T=[[False for _ in range (N)] for _ in range (N)]    
#     path=deepcopy(T)
#     def convert(L,T):
#         for el in L:
#             T[el[0]][el[1]]=True
#     convert(L,T)
#     def f(w,k):
#         if w==N-1 and k==N-1:
#             return 0,[(w,k)]
#         mini=float('inf'),[]
#         for i in range (k+1,N):
#             if T[w][i]==True:
#                 break
#             check=f(w,i)
#             if mini[0]>check[0]:
#                 mini=check
#         for j in range (w+1,N):
#             if T[j][k]==True:
#                 break
#             check=f(j,k)
#             if mini[0]>check[0]:
#                 mini=check
#         return 1+mini[0],mini[1]+[(w,k)]
#     return f(0,0)
# print(rook(8,[(0,3),(1,7),(2,5),(3,3),(4,6),(5,2),(6,7),(7,4),(6,5)]))

#z.B4
# def count_towers(T):
#     N=len(T)
#     row=col=[0]*N
#     for i in range (N):
#         for j in range (N):
#             if T[i][j]:
#                 row[i]+=1
#                 col[j]+=1
#     return row,col
# def move(T):
#     N=len(T)
#     a=count_towers(T)
#     row=a[0]
#     col=a[1]
#     dest_r,dest_c=N+1,N+1
#     for i in range (N):
#         if row[i]==0: #mamy pewność że maksymalnie w jednym wierszu i kolumnie bedzie 0  
#             dest_r=i
#         if col[i]==0:
#             dest_c=i
#         if dest_r!=N+1 and dest_c!=N+1:
#             break
#     if dest_r==N+1:
#         dest_r=0
#     if dest_c==N+1:
#         dest_c=0
#     destination=(dest_r,dest_c)
#     for i in range (N):
#         if row[i]<=1:
#             continue
#         for j in range(N):
#             if col[j]<=1:
#                 continue
#             if T[i][j]==True:
#                 return (i,j),destination
            
    
        