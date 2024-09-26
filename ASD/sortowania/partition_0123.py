def partition_4way(T):
    i,j = -1,-1
    k = 0
    l = len(T) - 1
    while k <= l:
        if T[k] == 1:
            j += 1
            T[j],T[k] = T[k],T[j]
            i += 1
            T[j],T[i] = T[i],T[j]
            k += 1
        elif T[k] == 2:
            j += 1
            T[j],T[k] = T[k],T[j]
            k += 1
        elif T[k] == 3:
            k += 1
        else:
            T[l],T[k] = T[k],T[l]
            l -= 1
    return T

print(partition_4way([1,1,2,3,3,2,4,3,2,4,4,3,2,1,2,3,4,2,1,3,2,1,2,4,4,2,3,1]))