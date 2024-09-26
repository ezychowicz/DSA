#f(i, j) - liczba ulozen konczacych sie na i-tym indeksie na wartosci j
#odp: f(length - 1, b)
#f(i, j) = f(i - 1, j - 1) + f(i - 1, j) + f(i - 1, j + 1) liczba ulozen do i tego indeksu o wartosci j to liczba ulozen do i - 1 indeksu o wartosciach j-1,j,j+1 
#2x2
a = 2
b = 2
length = 3
def possibilities(a, b, length):
    val_range = max(a,b) + length 
    F = [[0 for _ in range (val_range + 1)] for __ in range (length)]
    F[0][a] = 1
    for i in range (1, length): #indeksy
        for val in range (max(a,b) + length):
            F[i][val] = F[i - 1][val - 1] + F[i - 1][val + 1] + F[i - 1][val]
    return F[length - 1][b]

#
print(possibilities(a,b,length))