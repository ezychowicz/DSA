# def translate(a,p):
#     res=set()
#     while a!=0:
#         res.add(a%p)
#         a//=p
#     return res
# def check(a,b):
#     k=0
#     a_p,b_p=set(),set()
#     for p in range (2,17):
#         a_p=translate(a,p)
#         b_p=translate(b,p)
#         for el in set(a_p):
#             if el in b_p:
#                 k=1
#                 break
#         if k==0:
#             return p
#         k=0
#     return "brak odpowiedniej podstawy"
# print(check(123,522))
# N=1000

#suma wyrazow=suma elementow, spojny, rosnacy

# import random,time
# start=time.time()
# N=1000
# T=[0,1,5,4,2,5,546,34,46,9,10,11,12,9,18,15]
# print(T)
# max_c=-float('inf')
# count=1
# for start in range (len(T)-1):
#     if len(T)-1-start<max_c:
#         break
#     count=1
#     i=start
#     s_i=i
#     s=T[i]
#     while i<len(T)-1 and T[i+1]>T[i]:
#         s_i+=i+1
#         s+=T[i+1]
#         i+=1
#         count+=1
#         if s_i==s:
#             if max_c<count:
#                 max_c=count
# if max_c>1:
#     print(max_c)
# else:
#     print(0)
# end=time.time() 
# def traverse(T):
#     N=len(T)
#     cnt=1
#     maxi=1
#     i=1
#     while i<N-maxi:
#         suma,suma_i=T[i-1],i-1
#         j=i-1
#         cnt=1
#         while i<N and T[i]>T[i-1]:
#             suma+=T[i]
#             suma_i+=i
#             cnt+=1
#             if suma==suma_i:
#                 maxi=max(maxi,cnt)
#             i+=1
#         while j<i-1:
#             suma-=T[j]
#             suma_i-=j
#             cnt-=1
#             if suma==suma_i:
#                 maxi=max(maxi,cnt)
#                 break
#             j+=1
#         i+=1
#     return maxi if maxi>1 else 0
# print(end-start)
# start=time.time()
# print(traverse([0,1,5,4,2,5,546,34,46,9,10,11,12,9,18,15]))
# end=time.time()
# print(end-start)

#kolokwium 2
#z.2
# from copy import deepcopy
# def is_prime(a):
#     return a in (2,3,5,7)
# def zad2(t):
#     t[0]=1
#     v=[False]*10 #gdy v[i]=True to i użyte
#     v[1]=True
#     def f(t,p,v):
#         if p==8:
#             print(t)
#             return
#         for i in range (2,10):
#             if abs(t[p]-i)>=2 and not v[i]:
#                 if ((is_prime(t[p]) and not is_prime(i)) or not is_prime(t[p])):
#                     v[i]=True
#                     t[p+1]=i
#                     f(t,p+1,v) 
#                     t[p+1]=0
#                     v[i]=False
#         return 
#     f(t,0,v)
# print(zad2([0]*9))

#kolokwium 2 z.2 gr B
# def zad2(t):
#     N=len(t)
#     def f(a,b,len_a,len_b,p):
#         if len_a==len_b and a==b and len_a!=0:
#             return True
#         if p==N or abs(len_a-len_b)>N-p:
#             return False
#         return f(a+t[p],b,len_a+1,len_b,p+1) or f(a,b+t[p],len_a,len_b+1,p+1) or f(a,b,len_a,len_b,p+1)
#     return f(0,0,0,0,0)
# print(zad2([6,47,5,43,35,6565,5,4,6,4,5,7,5,5,3,753,45,2]))


#kolokwium poprawkowe
#z.1
# def cut(t,suma,curr_sum,p,cnt):
#     if p==len(t):
#         if suma==curr_sum:
#             return cnt+1
#         return 0
#     if suma==curr_sum:
#         return max(cut(t,suma,0,p,cnt+1),cut(t,suma,curr_sum+t[p],p+1,cnt))
#     return cut(t,suma,curr_sum+t[p],p+1,cnt)




# t=[1,2,3,1,5,5,-2,3,6,1,2,3,1,5,5,-2,3,6,1,2,3,1,5,5,-2,3,6,5,-2,3,6,5,-2,3,6,5,-2,3,6,9,-2,3,6,1,2,3,1,5,-2,3,6,1,2,3,1,5,-2,3,6,1,2,3,1,5,5,5,-2,3,6,5,-2,3,6,5,-2,3,6,5,-2,3,6,9,-2,3,6,1,2,3,1,5,-2,3,6,1,5,5,-2,3,6,5,-2,3,6,5,-2,3,6,5,-2,3,6,9,-2,3,6,1,2,3,1,5,-2,3,6,1,5,5,-2,3,6,5,-2,3,6,5,-2,3,6,5,-2,3,6,9,-2,3,6,1,2,3,1,5,-2,3,6,1,5,5,-2,3,6,5,-2,3,6,5,-2,3,6,5,-2,3,6,9,-2,3,6,1,2,3,1,5,-2,3,6,1]
# N=len(t)
# res=0
# zadana_suma=0
# from time import time
# start=time()
# for i in range (N-1):
#     zadana_suma+=t[i]
#     res=max(cut(t,zadana_suma,0,i+1,0)+1,res)
# print(res)
# end=time()
# print(end-start)
# print("_________")









# maxi=0
# def cut(t,suma,curr_sum,p,cnt):
#     global maxi
#     if p==len(t):
#         if suma==curr_sum:
#             maxi=max(maxi,cnt+1)
#         return 
#     if suma==curr_sum:
#         cut(t,suma,0,p,cnt+1)
#     cut(t,suma,curr_sum+t[p],p+1,cnt)
#     return

# N=len(t)
# zadana_suma=0
# start=time()
# for i in range (N-1):
#     zadana_suma+=t[i]
#     #print("zadana suma:",zadana_suma)
#     cut(t,zadana_suma,0,i+1,0)
# print(maxi+1)
# end=time()
# print(end-start)











# def f(suma,p,goal):
#     if p==N:
#         if suma==goal:
#             return 1
#         return -float('inf')
#     maxi=-float('inf')
#     maxi=max(maxi,f(suma+t[p],p+1,goal))
#     if suma==goal:
#         maxi=max(maxi,f(t[p],p+1,goal)+1)
#     return maxi


# N=len(t)
# zadana_suma=0
# start=time()
# res=0
# for i in range (N-2):
#     zadana_suma+=t[i]
#     res=max(res,f(t[i+1],i+2,zadana_suma))
# print(res+1)
# end=time()
# print(end-start)




#z.2 poprawkowy

def zad(t1,t2):
    N=len(t1)
    def f(t1_cnt,t2_cnt,suma_1,suma_2,p):
        if p==N:
            if t1_cnt==t2_cnt and suma_1==suma_2:
                return t1_cnt
            return 0
        add_1=f(t1_cnt+1,t2_cnt,suma_1+t1[p],suma_2,p+1)
        add_2=f(t1_cnt,t2_cnt+1,suma_1,suma_2+t2[p],p+1)
        add_12=f(t1_cnt+1,t2_cnt+1,suma_1+t1[p],suma_2+t2[p],p+1)
        skip_12=f(t1_cnt,t2_cnt,suma_1,suma_2,p+1)
        return max(add_1,add_2,add_12,skip_12)
    return f(0,0,0,0,0)
print(zad([4,5,7,3,4,8,4,37,5],[7,4,32,78,2,6,4,3,8]))

# 2sp

def zad(t1,t2):
    maxi=0
    N=len(t1)
    def f(t1_cnt,t2_cnt,suma_1,suma_2,p):
        nonlocal maxi
        if p==N:
            if t1_cnt==t2_cnt and suma_1==suma_2:
                maxi=max(maxi,t1_cnt)
                return 
            return 
        f(t1_cnt+1,t2_cnt,suma_1+t1[p],suma_2,p+1)
        f(t1_cnt,t2_cnt+1,suma_1,suma_2+t2[p],p+1)
        f(t1_cnt+1,t2_cnt+1,suma_1+t1[p],suma_2+t2[p],p+1)
        f(t1_cnt,t2_cnt,suma_1,suma_2,p+1)
        return 
    f(0,0,0,0,0)
    return maxi
print(zad([4,5,7,3,4,8,4,37,5],[7,4,32,78,2,6,4,3,8]))