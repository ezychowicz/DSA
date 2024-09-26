#basic
def bin_search(T,key):
    left = 0
    right = len(T) - 1
    while left < right:
        mid = (left+right)//2
        if T[mid] == key:
            right = mid
        elif T[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return left

def bin_search(T,key): #element mniejszy badz rowny key, ale max na prawo
    left = 0
    right = len(T) - 1
    while left < right:
        mid = (left + right + 1)//2 #kluczowe
        if T[mid] <= key:
            left = mid
        else:
            right = mid - 1
    return left

def bin_search(T,key): #element wiekszy badz rowny key, ale max na lewo
    left = 0
    right = len(T) - 1
    while left < right:
        mid = (left + right)//2 
        if T[mid] >= key:
            right = mid
        else:
            left = mid + 1
    return left


T = [7,7,7,8,8]

print(bin_search(T,7))