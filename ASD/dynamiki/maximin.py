#f(i,k) - maksymalna wartosc podzialu od i-tego wyrazu wlacznie do konca z k przedzialami
#O(n^2*k)
def maximin(T, K):
    prefixSum = T[::]
    for i in range (1, len(T)):
        prefixSum[i] += prefixSum[i - 1] 
    def sum_between(i,j): #suma od i-tego do j-tego wyrazu włącznie
        if i == 0:
           return prefixSum[j]
        return prefixSum[j] - prefixSum[i - 1]
    F = [[-float('inf') for j in range (K + 1)] for i in range (len(T))]
    #base case:
    for i in range (len(T)):
        #print(sum_between(i,len(T) - 1))
        F[i][1] = sum_between(i,len(T) - 1) #1 przedzial no to po prostu calosc

    for k in range (2, K + 1):
        for i in range (len(T) - 1, -1, -1):
            maxi = -float('inf')
            for j in range (len(T) - 1, i, -1):
                #print(F[j][k - 1],sum_between(i,j))
                maxi = max(maxi, min(F[j][k - 1], sum_between(i,j - 1)))
            F[i][k] = max(maxi,F[i][k])
    #print(F)
    return F[0][K]

#O(nklogn)
def maximin(T, K):
    def binary(i): #nie do konca binary search, tylko po porostu metoda eliminacji przypadkow niemozliwych
        maxi = -float('inf')
        left, right = i, len(T) - 1
        while left <= right:
            mid = (left + right)//2
            sum = sum_between(left, mid)
            rest = F[mid + 1][k - 1]
            maxi = max(maxi, min(sum,rest))
            if sum > rest:
                left = mid + 1 #nie musimy sie zabezpieczac i robic left = mid np. bo juz i tak zapisalismy left = mid
            else:
                right = mid - 1 
        return maxi
    prefixSum = T[::]
    for i in range (1, len(T)):
        prefixSum[i] += prefixSum[i - 1] 
    def sum_between(i,j): #suma od i-tego do j-tego wyrazu włącznie
        if i == 0:
           return prefixSum[j]
        return prefixSum[j] - prefixSum[i - 1]
    F = [[-float('inf') for j in range (K + 1)] for i in range (len(T))]
    #base case:
    for i in range (len(T)):
        F[i][1] = sum_between(i,len(T) - 1) #1 przedzial no to po prostu calosc

    for k in range (2, K + 1):
        for i in range (len(T) - 1, -1, -1):           
            F[i][k] = binary(i)
    return F[0][K]

    