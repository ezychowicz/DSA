#O(n^2)
def coal(A,T):
    N = len(A)
    storages = [T]*N
    for delivery in A:
        i = 0
        while storages[i] < delivery:
            i += 1
        storages[i] -= delivery
    return i

print(coal([1,6,2,10,8,7,1],10))

