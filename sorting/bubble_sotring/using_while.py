# Эффективен для массивов небольшого размера. Сложность O(n^2)
from random import randint


list_ = []
N=10

for i in range(N):
    list_.append(randint(1, 99))

print(list_)

i = 0

while i < N-1:
    j = 0
    while j < N-1-i:
        if list_[j] > list_[j+1]:
            list_[j], list_[j+1] = list_[j+1], list_[j]
        j += 1
    i+=1

print(list_)
