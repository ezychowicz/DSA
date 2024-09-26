# import random
# def sum_tab(tab, ix, l):
#     sum=0
#     for i in range (ix,ix+l):
#         sum+=tab[i]
#     return tab

# def is_pow(x):
#     a=2
#     while a<=(x**(1/2)):
#         x_copy=x
#         while x_copy%a==0: x_copy//=a
#         if x_copy==1: return True
#         a+=1
#     return False

# print(is_pow(36))
# def zad1(t1, t2):
#     n=len(t1)
#     for i in range (1,24):
#         for ix1 in range (n-i+1):
#             for ix2 in range (n-(24-i)+1):
#                 sum=sum_tab(t1,ix1,i)+sum_tab(t2,ix2,24-i)
#                 if is_pow(sum): return True
#     return False
# #poprawkowy 
# #z.1
# def nwd(a,b):
#     while b!=0:
#         a,b=b,a%b
#     return a
# def nwd_4(a,b,c,d):
#     res=a
#     for el in (b,c,d):
#         res=nwd(res,el)
#         if res>1:
#             return False
#     return True

# def ustaw(T):
#     N=len(T)
#     for i in range (N):
#         for j in range (N):
#             for k in range (N):
#                     if k!=i:
#                         for l in range (N):
#                             if j!=l:
#                                 for el1 in ((0,-1),(0,1)):
#                                     for el2 in ((-1,0),(1,0)):
#                                         if 0<=el1[1]+j<N and 0<=el2[0]+k<N and l!=el1[1]+j and i!=el2[0]+k and nwd_4(T[i][j],T[k][l],T[k+el2[0]][l],T[i][j+el1[1]]):
#                                             print(T[i][j],T[k][l],T[k+el2[0]][l],T[i][j+el1[1]])
#                                             return True
#     return False

# import random
# T=[[random.randint(1,100) for _ in range (100)] for _ in range (10)]
# # print(ustaw(T))

# #z.2
# #czy można usunąć jeden wiersz 2 kolumny
# def binary(a):
#     cnt=0
#     while a>0:
#         if a%2==1:
#             cnt+=1
#         a//=2
#     return cnt%2==1
# def convert(T):
#     N=len(T)
#     for i in range (N):
#         for j in range (N):
#             T[i][j]=binary(T[i][j])
# def sum_cols(T):
#     N=len(T)
#     cols=[0]*N
#     for i in range (N):
#         for j in range (N):
#             if not T[i][j]:
#                 cols[j]+=T[i][j]
#     return cols
# print(sum_cols(T))
# def traverse(T):
#     convert(T)
#     cols=sum_cols(T)
#     N=len(T)
#     for rows in range (N):
#         cnt=0
#         for i in range (N):
#             if (T[rows][i]==False and cols[i]-1>0) or (T[rows][i]==True and cols[i]>0):
#                 cnt+=1
#             if cnt>2:
#                 break
#             if i==N-1:
#                 return True
#     return False

#z.2A
def zad2(X,Y,N):
    def operation_c(a):
        cnt=0
        c_a=0
        while a>0:
            if a%2==0:
                c_a+=(a%10+1)*10**(cnt)
            else:
                c_a+=a%10*10**(cnt)
            cnt+=1
            a//=10
        return c_a
    def operation_c2(a):
        cnt=0
        c_a=0
        while a>0:
            if a%2!=0:
                c_a+=(a%10-1)*10**(cnt)
            else:
                c_a+=a%10*10**(cnt)
            cnt+=1
            a//=10
        return c_a
    



    def f(X,N,prev):
        cnt=0
        if X==Y:
            return 1
        if N==0 or X>Y:
            return 0
        if prev=="":
            cnt+=f(X+3,N-1,"A")+f(X*2,N-1,"B")+f(operation_c(X),N-1,"C")
        if prev=="A":
            cnt+=f(X*2,N-1,"B")+f(operation_c(X),N-1,"C")
        if prev=="B":
            cnt+=f(X+3,N-1,"A")+f(operation_c(X),N-1,"C")
        if prev=="C":
            cnt+=f(X*2,N-1,"B")+f(X+3,N-1,"A")
        return cnt
    


    def f2(X,N,prev,path):
        if N==0 and X!=Y: 
            return float('inf')
        if X==Y:
            #print(path)
            return 0
        mini=float('inf')
        if prev=="":
            mini=min(f2(X+3,N-1,"A",path+"A"),f2(X*2,N-1,"B",path+"B"),f2(operation_c2(X),N-1,"C",path+"C"))
        elif prev=="A":
            mini=min(f2(X*2,N-1,"B",path+"B"),f2(operation_c2(X),N-1,"C",path+"C"))
        elif prev=="B":
            mini=min(f2(X+3,N-1,"A",path+"A"),f2(operation_c2(X),N-1,"C",path+"C"))
        elif prev=="C":
            mini=min(f2(X*2,N-1,"B",path+"B"),f2(X+3,N-1,"A",path+"A"))
        return 1+mini
    import time
    start=time.time()
    res=f2(X,N,"","")
    end=time.time()
    print(end-start)
    print(res)
    mini=float('inf')



    def f3(X,cnt,prev,path):
        nonlocal mini
        if cnt==N and X!=Y: 
            return float('inf')
        if X==Y:
            if mini>cnt:
                mini=cnt
            return
        # if mini<cnt:
        #     return 
        if prev=="":
            f3(X+3,cnt+1,"A",path+"A")
            f3(X*2,cnt+1,"B",path+"B")
            f3(operation_c2(X),cnt+1,"C",path+"C")
        elif prev=="A":
            f3(X*2,cnt+1,"B",path+"B")
            f3(operation_c2(X),cnt+1,"C",path+"C")
        elif prev=="B":
            f3(X+3,cnt+1,"A",path+"A")
            f3(operation_c2(X),cnt+1,"C",path+"C")
        elif prev=="C":
            f3(X*2,cnt+1,"B",path+"B")
            f3(X+3,cnt+1,"A",path+"A")
        return 




    start=time.time()
    f3(X,0,"","")
    end=time.time()
    print(end-start)
    return mini if mini!=float('inf') else -1

    #return res if res!=float('inf') else -1
print(zad2(23,27,5))

#z.3 kolokwium I
# def zad3():
#     N=4
#     import random
#     T=[[random.randint(-10,10) for _ in range (N)] for _ in range (N)]
#     def f(row,prev,suma):
#         print(suma)
#         if row==N and suma==0:
#             return True
#         if row==N:
#             return False
#         for i in range (N):
#             if i not in range (prev-1,prev,prev+1):
#                 if f(row+1,i,suma+T[row][i]):
#                     return True
#         return False
#     return f(0,N+10,0)
# print(zad3())

#z.2 poprawkowe mag-mino
# def zad(T):
#     N=len(T)
#     v=[False]*N
#     def f(v,next,curr):
#         maxi=0,[]
#         for i in range (N):
#             if not v[i]:
#                 if next==T[i][0]:
#                     v[i]=True
#                     check=f(v,T[i][1],i)
#                     v[i]=False
#                     if maxi[0]<check[0]:
#                         maxi=check
#                 elif next==T[i][1]:
#                     v[i]=True
#                     check=f(v,T[i][0],i)
#                     v[i]=False
#                     if maxi[0]<check[0]:
#                         maxi=check 
#         return 1+maxi[0],maxi[1]+[T[curr]]
#     max_len=0
#     res=[]
#     for i in range (N): #aby zacząć od każdej liczby z domina
#         v[i]=True
#         check_1=f(v,T[i][0],i)
#         if max_len<check_1[0]:
#             max_len=check_1[0]
#             res=check_1[1]
#         check_2=f(v,T[i][1],i)
#         if max_len<check_2[0]:
#             max_len=check_2[0]
#             res=check_2[1]  
#         v[i]=False
#     return max_len,res
# print(zad([[2,8],[0,1],[2,3],[3,6],[2,6],[2,9],[3,4],[6,7]]))
# def zad(T):
#     N=len(T)
#     def f(w,prev,suma):
#         print(w,prev,suma)
#         if w==N and suma==0:
#             return True
#         if w==N:
#             return False
#         for i in range (N):
#             if i!=prev-1 and i!=prev and i!=prev+1:
#                 if f(w+1,i,suma+T[w][i]):
#                     return True
#         return False
#     return f(0,float('inf'),0)
# import random
# T=[[random.randint(-10,10) for _ in range (10)] for _ in range (10)]
# print(zad(T))

# def zad(T):                       #czy tutaj to odznaczanie col działa tak jak powinno?
#     N=len(T)
#     def f(w,col,suma):
#         print(w,col,suma)
#         if w==N and suma==0:
#             return True
#         if w==N:
#             return False
#         for i in range (N):
#             if not col[i]:
#                 for el in (-1,0,1):
#                     if 0<=el+i<N:
#                         col[el+i]=True
#                 if f(w+1,col,suma+T[w][i]):
#                     return True
#                 for el in (-1,0,1):
#                     if 0<=el+i<N:
#                         col[el+i]=False
#         return False
#     return f(0,[False]*N,0)
# import random
# T=[[random.randint(-10,10) for _ in range (10)] for _ in range (10)]
# print(zad(T))