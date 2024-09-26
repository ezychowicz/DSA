#f(k) - ilosc sposobow rozlozenia k na liczby z A=[1,2,3,4,5,6]
#f(k) = sum(i<=5)(f(k - A[i]))  
def dice(n):
    F = [0]*(n + 1)
    F[0] = F[1] = 1 #F[0] bedzie mialo wplyw na wyniki dla 1 2 3 4 5 6, bo mozemy uzyskac np. 3 biorac po prostu 3
    for k in range (2,n + 1):
        for i in range (1,7):
            if k - i < 0:
                break
            F[k] += F[k - i]
    return F[n]

print(dice(10))