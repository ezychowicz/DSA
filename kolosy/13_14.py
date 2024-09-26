#zad.1 - sliding window z chamskimi przypadkami skrajnymi ktore trzeba oddzielnie
tab=[0]*5
i=0
def push(num,tab):
    prev=tab[-1]
    tab[-1]=num
    i=2
    while i<=5:
        tab[-i],prev=prev,tab[-i]
        i+=1

while i<5:
    k=int(input("liczba: "))
    tab[i]=k
    i+=1
suma=sum(tab)
for left in range (3):
    print(tab)
    if tab[left]==(suma-tab[left])/4:
        print(tab[left])
k=int(input("liczba: "))
while k!=0:
    suma+=k-tab[0]
    push(k,tab)
    print(tab)
    if tab[left]==(suma-tab[left])/4:
        print(tab[left])
    k=int(input("liczba: "))
left+=1
for i in range (2):
    if tab[left+i]==(suma-tab[left+i])/4:
        print(tab[left+i])

#zad.2
#w wdi_6.py jest