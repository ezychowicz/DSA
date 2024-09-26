# # #z.1
# # def multi(T):
# #     N=len(T)
# #     for lens in range ((N//2),0,-1):
# #         if N%lens==0:
# #             for i in range (lens):
# #                 j=lens
# #                 while i+j<N:
# #                     if T[i]!=T[i+j]:
# #                         break
# #                     j+=lens 
# #                 else:
# #                     return lens
# #     return 0
# # print(multi(list("AAAAA")))
# #Poprawkowy
# #z.1
# # def zeroes(T):
# #     N=len(T)
# #     cnt=2
# #     maxi=2
# #     for i in range (2,N):
# #         if T[i][0]==T[i-1][0] and T[i][0]==0: #(0,0,0,0) ma dlugosc 4 ale (k,0,0,0,0) juz dlugosc 5 pomimo ze zer tyle samo 
# #             cnt+=1
# #         else:
# #             maxi=max(maxi,cnt)
# #             cnt=2
# #     return max(maxi,cnt)
# # def NWD(a,b):
# #     if a==0:
# #         return 1
# #     while b!=0:
# #         a,b=b,a%b
# #     return a
# # def zad1(T):
# #     N=len(T)
# #     cnt=2
# #     maxi=2
# #     if T[1][0]*T[0][0]!=0:
# #         nwd=NWD(T[0][0]*T[1][1],T[0][1]*T[1][0])
# #         q=((T[0][0]*T[1][1])//nwd,T[0][1]*T[1][0]//nwd)
# #     else:
# #         q=(1/2,1/2)
# #     for i in range (2,N):
# #         if T[i][0]*T[i-1][0]==0:
# #             continue
# #         nwd=NWD(T[i-1][1]*T[i][0],T[i-1][0]*T[i][1])
# #         q_curr=((T[i-1][1]*T[i][0])//nwd,T[i-1][0]*T[i][1]//nwd)
# #         print(q_curr,i)
# #         if q_curr==q:
# #             cnt+=1
# #         else:
# #             q=q_curr
# #             maxi=max(maxi,cnt)
# #             cnt=2
# #     return max(maxi,cnt,zeroes(T)) if max(maxi,cnt,zeroes(T))>2 else 0
# # print(zad1( [(1,2),(0,3),(0,4),(0,5),(5,6)]))
# # print("----------------")
# # #z.2
# # def cutting(s):
# #     single=['a','e','i','o','u','y']
# #     N=len(s)
# #     i_save=0
# #     flag=True
# #     res=1
# #     for i in range (N):
# #         if s[i] in single:
# #             print(s[i])
# #             if flag==True: 
# #                 flag=False
# #             else:
# #                 res*=i-i_save
# #             i_save=i
# #     return res
# # print(cutting("studentdebil"))
# #rekurencyjnie:
# # def cutting(s):
# #     N=len(s)
# #     def is_samo(a):
# #         if a in ("a","e","y","u","i","o"):
# #             return 1
# #         else:
# #             return 0
# #     def f(p,samo):
# #         cnt=0
# #         if p==N and samo!=0:
# #             return 1
# #         if p==N:
# #             return 0
# #         if samo==0:
# #             cnt+=f(p+1,samo+is_samo(s[p]))
# #         if samo==1 and is_samo(s[p])==0:
# #             cnt+=f(p+1,samo)+f(p,0)
# #         elif samo==1 and is_samo(s[p])==1:
# #             cnt+=f(p,0)
# #         return cnt
# #     return f(0,0)
# # print(cutting("informatyka"))
# #z.4
# # def is_prime(a):
# #     if a<2:
# #         return False
# #     if a==2:
# #         return True
# #     if a%2==0:
# #         return False
# #     i=3
# #     while i<=a**(0.5):
# #         if a%i==0: 
# #             return False
# #         i+=2
# #     return True
# # def f(N,curr,cnt):
# #     if N==0:
# #         return is_prime(curr) and is_prime(cnt+1) 
# #     return (is_prime(curr) and f(N%10**(len(str(N))-1),N//10**(len(str(N))-1),cnt+1)) or f(N%10**(len(str(N))-1),curr*10+N//10**(len(str(N))-1),cnt)
# # print(f(23672,0,0))

# def divide(N):
#     def is_prime(a):
#         if a<2:
#             return False
#         if a==2:
#             return True
#         if a%2==0:
#             return False
#         i=3
#         while i<=a**(0.5):
#             if a%i==0: 
#                 return False
#             i+=2
#         return True
#     path=[0]*(len(str(N)))
#     def f(p,N,dlg,cnt,path):
#         #nonlocal path
#         if p>=dlg:
#             if is_prime(N) and is_prime(cnt):
#                 path[cnt-1]=N//10**(dlg-p)
#                 print(path)                 
#                 return True
#             return False
#         if is_prime(N//10**(dlg-p)):
#             path[cnt-1]=N//10**(dlg-p)
#             if f(1,N%10**(dlg-p),dlg-p,cnt+1,path):
#                 #path[cnt-1]=N//10**(dlg-p)
#                 return True
#             path[cnt-1]=0
#         return f(p+1,N,dlg,cnt,path)
#     return f(1,N,len(str(N)),1,path)#,path
# print(divide(23672))


#f(i,p) - max pojemnosc dla akademikow do konca i-tego akademika na osi, o koszcie calosciowym <=p. zakladam ze biore i-ty budynek
#odp: max(i)(f(i,p)), gdy maxi = F[][]: minimalne p
# def select_buildings(T, p):
#     def restore_path(i, p_maxi):
#         path = []
#         p = p_maxi
#         while (i,p) != (None, None):
#             path.append(T[i][4]) #dodaj indeks budynku
#             i, p = par[i][p] 
#         path.reverse()
#         return path
    
#     def capacity(el):
#         return (el[2] - el[1])*el[0]
#     def w(el):
#         return el[3]
#     def b(el):
#         return el[2]
#     def a(el):
#         return el[1]
#     P = p
#     p = 0
#     for i in range (len(T)):
#         T[i] = (T[i][0], T[i][1], T[i][2], T[i][3], i)
    
#     T.sort(key = lambda x: x[1]) #sortuj po końcach budynków
#     F = [[-float('inf') for p in range (P + 1)] for i in range (len(T))]
#     par = [[(None,None) for p in range (P + 1)] for i in range (len(T))] #parent
    
#     for p in range (w(T[0]), P + 1):
#         F[0][p] = capacity(T[0])

#     for i in range (1, len(T)):
#         for p in range (P + 1):
#             if w(T[i]) <= p:
#                 F[i][p] = capacity(T[i])  #jesli cena jest ok to zawsze mozna wziac sam ten budynek (wtedy brak parenta)
#             for j in range (i):
#                 if b(T[j]) < a(T[i]): #jesli dla zadnego nie bedzie spelnione to znaczy ze nachodzi z kazdym budynkiem przed nim
#                     if F[i][p] < F[j][p - w(T[i])] + capacity(T[i]):
#                         par[i][p] = (j, p - w(T[i]))
#                     F[i][p] = max(F[i][p], F[j][p - w(T[i])] + capacity(T[i]))
                    
#     maxi = -float('inf')
#     p_maxi = P
#     for i in range (len(T)):
#         for p in range (P + 1):
#             if maxi < F[i][p]:
#                 maxi = F[i][p]
#                 p_maxi = p
#                 i_maxi = i
#             elif maxi == F[i][p]:
#                 p_maxi = min(p_maxi, p)
#                 i_maxi = i
#     print(F[i_maxi][p_maxi])
#     return restore_path(i_maxi, p_maxi)


# T = [ (2, 1, 5, 3),
# (3, 7, 9, 2),
# (2, 8, 11, 1) ]
# p = 5

# print(select_buildings(T,p))
                                    
