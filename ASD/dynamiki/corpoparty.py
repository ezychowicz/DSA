class Employee:
    def __init__(self,fun):
        self.emp = []
        self.fun = fun
        self.f = -1
        self.g = -1
        self.taken = False
def f(v):
    if v.f >= 0:
        return v.f
    v.f = g(v)
    suma = v.fun
    for employee in v.emp: 
        suma += g(employee)
    if suma > v.f:
        v.f = suma
        v.taken = True
    return v.f
def g(v):
    if v.g >= 0:
        return v.g
    v.g = 0
    for employee in v.emp:
        v.g += f(employee)
    return v.g

a = Employee(10)
b = Employee(10)
c = Employee(25)
d = Employee(5)
e = Employee(5)
h = Employee(5)
i = Employee(10)
j = Employee(5)
k = Employee(20)
a.emp = [b,c,d]
b.emp = [e,h]
c.emp = [i]
d.emp = [j]
i.emp = [k]
print(f(a))