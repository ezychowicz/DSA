#sum query and update values: find the sum of a[l:r] O(logn), update i-th value O(logn)
def sum_query():
    def left(i):
        return 2*i + 1
    def right(i):
        return 2*i + 2
    def parent(i):
        return (i - 1)//2


    def build(T, a, l, r, i): #funkcja buduje tablice T, ktora reprezentuje kopiec o wartościach bedących sumami czesciowymi z a. W szczegolnosci liść to wartość z tablicy a, T[i] = suma od jakiegos l do jakiegos r, nie jest to explicite podane
        if l == r:
            T[i] = a[l]
        else:
            mid = (l + r)//2
            build(T, a, l, mid, left(i))
            build(T, a, mid + 1, r, right(i))
            T[i] = T[left(i)] + T[right(i)]

    def sum(T, input_l, input_r):
        def rec(l, r, i):
            if l == r: #bo sie blokuje gdy jest l=r
                return T[i]
            if (l,r) == (input_l, input_r):
                return T[i]
            mid = (l + r)//2
            if input_l > mid:
                return rec(mid + 1, r, right(i))
            elif input_r <= mid:
                return rec(l, mid, left(i))
            else:
                return rec(l, mid, left(i)) + rec(mid + 1, r, right(i))
        return rec(0, len(a) - 1, 0) 

    def update(T, l, r, i, val, val_idx): #zmien strukture gdy zmieniono a[val_idx] na val
        if l == r: #to znaczy ze znalezlismy liścia do zmiany
            T[i] = val
            return
        mid = (l + r)//2
        if val_idx <= mid: #liść do zmainy po lewej 
            update(T, l, mid, left(i), val, val_idx)
        else:
            update(T, mid + 1, r, right(i), val, val_idx)
        T[i] = max(T[left(i)], T[right(i)])

    a = [1,2,3,4,5,6,7,8,9,10]
    T = [0]*(4*len(a))

    build(T, a, 0, len(a) - 1, 0)
    #print(T)
    print(sum(T,2,4))
    update(T,0, len(a) - 1, 0, 10, 3)
    print(sum(T,2,4))
sum_query()

def maximum():
    def left(i):
        return 2*i + 1
    def right(i):
        return 2*i + 2
    def parent(i):
        return (i - 1)//2


    def build(T, a, l, r, i): #funkcja buduje tablice T, ktora reprezentuje kopiec o wartościach bedących sumami czesciowymi z a. W szczegolnosci liść to wartość z tablicy a, T[i] = suma od jakiegos l do jakiegos r, nie jest to explicite podane
        if l == r:
            T[i] = a[l]
        else:
            mid = (l + r)//2
            build(T, a, l, mid, left(i))
            build(T, a, mid + 1, r, right(i))
            T[i] = max(T[left(i)], T[right(i)])

    def maxi(T, input_l, input_r):
        def rec(l, r, i):
            if l == r: #bo sie blokuje gdy jest l=r
                return T[i]
            if (l,r) == (input_l, input_r):
                return T[i]
            mid = (l + r)//2
            if input_l > mid:
                return rec(mid + 1, r, right(i))
            elif input_r <= mid:
                return rec(l, mid, left(i))
            else:
                return max(rec(l, mid, left(i)), rec(mid + 1, r, right(i)))
        return rec(0, len(a) - 1, 0) 

    def update(T, l, r, i, val, val_idx): #zmien strukture gdy zmieniono a[val_idx] na val
        if l == r: #to znaczy ze znalezlismy liścia do zmiany
            T[i] = val
            return
        mid = (l + r)//2
        if val_idx <= mid: #liść do zmainy po lewej 
            update(T, l, mid, left(i), val, val_idx)
        else:
            update(T, mid + 1, r, right(i), val, val_idx)
        T[i] = max(T[left(i)], T[right(i)])

    a = [1,2,3,4,5,6,7,8,9,10]
    T = [0]*(4*len(a))
    build(T, a, 0, len(a) - 1, 0) 
    print(maxi(T,2,9))

maximum()

def maximum_and_occurences(): #find the maximum and how many times it appears
    def left(i):
        return 2*i + 1
    def right(i):
        return 2*i + 2
    def parent(i):
        return (i - 1)//2


    def build(T, a, l, r, i): #funkcja buduje tablice T, ktora reprezentuje kopiec o wartościach bedących sumami czesciowymi z a. W szczegolnosci liść to wartość z tablicy a, T[i] = suma od jakiegos l do jakiegos r, nie jest to explicite podane
        if l == r:
            T[i] = (a[l], 1)
        else:
            mid = (l + r)//2
            build(T, a, l, mid, left(i))
            build(T, a, mid + 1, r, right(i))
            if T[left(i)][0] == T[right(i)][0]:
                T[i] = (T[left(i)][0], T[left(i)][1] + T[right(i)][1])
            elif T[left(i)][0] > T[right(i)][0]:
                T[i] = (T[left(i)][0], T[left(i)][1])
            else:
                T[i] = (T[right(i)][0], T[right(i)][1])

    def maxi(T, input_l, input_r):
        def rec(l, r, i):
            if l == r: #bo sie blokuje gdy jest l=r
                return T[i]
            if (l,r) == (input_l, input_r):
                return T[i]
            mid = (l + r)//2
            if input_l > mid:
                return rec(mid + 1, r, right(i))
            elif input_r <= mid:
                return rec(l, mid, left(i))
            else: #jesli interesujacy nas przedzial jest po obu stronach mid
                lefty = rec(l, mid, left(i))
                righty = rec(mid + 1, r, right(i))
                if lefty[0] > righty[0]:
                    return lefty
                elif lefty[0] < righty[0]:
                    return righty
                else:
                    return lefty[0], lefty[1] + righty[1]
                
        return rec(0, len(a) - 1, 0) 

    def update(T, l, r, i, val, val_idx): #zmien strukture gdy zmieniono a[val_idx] na val
        if l == r: #to znaczy ze znalezlismy liścia do zmiany
            T[i] = val
            return
        mid = (l + r)//2
        if val_idx <= mid: #liść do zmiany po lewej 
            update(T, l, mid, left(i), val, val_idx)
        else:
            update(T, mid + 1, r, right(i), val, val_idx)
        if T[left(i)][0] == T[right(i)][0]:
            T[i] = (T[left(i)][0], T[left(i)][1] + T[right(i)][1])
        elif T[left(i)][0] > T[right(i)][0]:
            T[i] = (T[left(i)][0], T[left(i)][1])
        else:
            T[i] = (T[right(i)][0], T[right(i)][1])

    a = [1,2,3,3,3,6,6,4,5,6,2,3,3,6,7,8,8,8,8,8,9,10,10,10]
    T = [(0,1) for _ in range (4*len(a))] #0,1 bo dla lisci sie zgadza wtedy i nie trzeba dodatkowo jakos pisac
    build(T, a, 0, len(a) - 1, 0) 
    print(maxi(T,2,9)) 

maximum_and_occurences()

#nwd mozna liczb od l do r mozna rozwiazac w dokladnie analogiczny sposob nwd(l,r) = nwd(T[left],T[right])
