#f(i, S) - czy istnieje podzbiór elementów z A[:i+1] (niekoniecznie zaw. A[i]) o sumie S 
#f(i, S) = f(i - 1, S - A[k]) (zał: S >= A[k]) or f(i - 1, S) #albo bierzemy i-ty element albo nie
#base case: i = 0: True gdy S = A[0]
#base case: S = 0: zawsze True
#rekurencyjnie z zapamietywaniem
def SSP1(A,T): #zbior, szukana suma
    F = [[-1 for _ in range (T + 1)] for __ in range (len(A))]
    for i in range (T + 1): #dla i = 0 true wtw. A[0] = suma
        if i != A[0]: 
            F[0][i] = 0
        else:
            F[0][i] = 1

    for i in range (len(A)):
        F[i][0] = 1 #sume 0 zawsze da sie uzyskac
    def f(k,S):
        if F[k][S] != -1:
            return F[k][S]
        F[k][S] = f(k - 1,S)
        if S >= A[k] and F[k][S] != 1:
            F[k][S] = f(k - 1,S - A[k])
        return F[k][S]
    
    return f(len(A) - 1,T)
  

#dp

def SSP2(A,T):
    F = [[-1 for _ in range (T + 1)] for __ in range (len(A))]

    for i in range (T + 1): #dla i = 0 true wtw. A[0] = suma
        if i != A[0]: 
            F[0][i] = 0
        else:
            F[0][i] = 1

    for i in range (len(A)):
        F[i][0] = 1 #sume 0 zawsze da sie uzyskac

    for i in range (1,len(A)):
        for S in range (1,T + 1):
            if S - A[i] < 0: #nie da sie wziac A[i], mozna jedynie nie brac
                F[i][S] = F[i - 1][S]
                continue
            if F[i - 1][S - A[i]]: #gdy bierzemy A[i] (abysmy otrzymali S biorąc A[i] musimy miec mozliwosc dostania S - A[i] z podzbioru po lewej)
                F[i][S] = 1
            if F[i][S] != 1: #gdy nie udalo sie biorąc A[i]
                F[i][S] = F[i - 1][S] #gdy nie bierzemy A[i]

    return F[len(A) - 1][T]

def test_SSP():
    test_cases = [
        ([3, 34, 4, 12, 5, 2], 9),
        ([1, 2, 3, 7], 6),
        ([1, 2, 7, 1, 5], 10),
        ([1, 3, 4, 8], 6),
        ([1,4,5,5], 11)
    ]

    for i, (A, T) in enumerate(test_cases):
        result1 = SSP1(A, T)
        result2 = SSP2(A, T)
        if result1 != result2:
            print(f"Test case {i+1} failed: A={A}, T={T}")
            print(f"SSP returned {result1}, but SSP2 returned {result2}")
            return
    print("All test cases passed.")

# Run the test
test_SSP()