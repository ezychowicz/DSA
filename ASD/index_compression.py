#zamiana punktow na indeksy
import random
positions = []
for i in range (30):
    positions.append([random.uniform(1,1000), random.uniform(1,1000)])

positions_set = set()
for el in positions:
    positions_set.add(el[0])
    positions_set.add(el[1])

positions_list = sorted(positions_set) #tak na prawde może być zwykla lista nie musi być posortowana, ale pomaga to w przewidywalności i powtarzalności algorytmu

dict = {}
idx = 0
for pos in positions_list:
    dict[pos] = idx
    idx += 1
print(positions)