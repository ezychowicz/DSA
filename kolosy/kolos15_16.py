#z.1 rek











def zad():
    from math import log,floor
    def dlg(a):
        if a!=0:
            return floor(log(a,10))+1
        return 1
    def op_a(a):
        if dlg(a)>=2:
            last=a%10
            prev=(a//10)%10
            a=(a//100)*100+last*10+prev
        return a
    def op_b(a):
        return 3*a
    def op_c(a):
        if dlg(a)>=2:
            return a%10**(dlg(a)-1)
        return a
    def f(x,y,N,path):
        if x==y:
            return path
        if N==0:
            return ""
        option1=f(op_a(x),y,N-1,path+"A")
        option2=f(op_b(x),y,N-1,path+"B")
        option3=f(op_c(x),y,N-1,path+"C")
        options=(option1,option2,option3)
        for i in range (3):
            if len(options[i])!=0:
                return options[i]
        return ""
    return f(17564,3,7,"")
print(zad())












#MINI-METODA 1

def zad():
    from math import log,floor
    def dlg(a):
        if a!=0:
            return floor(log(a,10))+1
        return 1
    def op_a(a):
        if dlg(a)>=2:
            last=a%10
            prev=(a//10)%10
            a=(a//100)*100+last*10+prev
        return a
    def op_b(a):
        return 3*a
    def op_c(a):
        if dlg(a)>=2:
            return a%10**(dlg(a)-1)
        return a
    def f(x,y,N,path):
        if x==y:
            return path
        if N==0:
            if x==y:
                return path
            return "aaaaaaaaaaa"
        option1=f(op_a(x),y,N-1,path+"A")
        option2=f(op_b(x),y,N-1,path+"B")
        option3=f(op_c(x),y,N-1,path+"C")
        options=(option1,option2,option3)
        mini="aaaaaaaaaaa"
        for i in range (3):
            if len(options[i])<len(mini):
                mini=options[i]
        return mini 
    res=f(17564,3,7,"")
    if res!="aaaaaaaaaaa":
        return res
    else:
        return ""
print(zad())








#MINI-METODA 2
def zad():
    from math import log,floor
    def dlg(a):
        if a!=0:
            return floor(log(a,10))+1
        return 1
    def op_a(a):
        if dlg(a)>=2:
            last=a%10
            prev=(a//10)%10
            a=(a//100)*100+last*10+prev
        return a
    def op_b(a):
        return 3*a
    def op_c(a):
        if dlg(a)>=2:
            return a%10**(dlg(a)-1)
        return a
    def f(x,y,N,curr):
        if x==y:
            return curr
        if N==0:
            return "aaaaaaaaaaa"
        mini="aaaaaaaaaaa"
        option1=f(op_a(x),y,N-1,"A")
        option2=f(op_b(x),y,N-1,"B")
        option3=f(op_c(x),y,N-1,"C")
        options=(option1,option2,option3)
        #print(options)
        for i in range (3):
            if len(options[i])<len(mini):
                mini=options[i]
        return curr+mini
    return f(17564,3,7,"")
print(zad())










#MINI-METODA 3 (nonlocal)
def zad():
    from math import log,floor
    def dlg(a):
        if a!=0:
            return floor(log(a,10))+1
        return 1
    def op_a(a):
        if dlg(a)>=2:
            last=a%10
            prev=(a//10)%10
            a=(a//100)*100+last*10+prev
        return a
    def op_b(a):
        return 3*a
    def op_c(a):
        if dlg(a)>=2:
            return a%10**(dlg(a)-1)
        return a
    mini="aaaaaaaaaaaaaa"
    def f(x,y,N,path):
        nonlocal mini
        if x==y:
            if len(mini)>len(path):
                mini=path[:]
            return 
        if N==0:
            return 
        f(op_a(x),y,N-1,path+"A")
        f(op_b(x),y,N-1,path+"B")
        f(op_c(x),y,N-1,path+"C")
        return 
    f(17564,3,7,"")
    return mini if len(mini)<8 else "nie da sie"
print(zad())

#z.2 poprawkowy

# def zad(t):
#     N=len(t)
#     def ones(a):
#         cnt=0
#         while a>0:
#             if a%2==1:
#                 cnt+=1
#             a//=2
#         return cnt
#     def f(a,b,c,p):
#         if p==N:
#             if a==b==c:
#                 return True
#             return False
#         return f(a+ones(t[p]),b,c,p+1) or f(a,b+ones(t[p]),c,p+1) or f(a,b,c+ones(t[p]),p+1)
#     return f(0,0,0,0)

# print(zad([2,3,5,7,11,13,16]))