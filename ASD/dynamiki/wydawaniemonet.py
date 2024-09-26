#A = [8,5,1] T = 15
#wydac T przy jak najmniejszej liczbie monet
#f(R) - najmniejsza liczba monet do wydania kwoty R 
#f(R) = minimum po i z (f(R - A[i]))
#O(n*T)

def wydawanie(T,A):
    F = [float('inf')]*(T + 1)
    F[0] = 0
    for i in range (1,T + 1):
        mini = float('inf')
        for coin in A:
            if F[i - coin] + 1 < F[i]:
                F[i] = F[i - coin] + 1
    return F[-1]
print(wydawanie(15, A = [8,5,1]))