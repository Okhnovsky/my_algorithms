# Эффективен для массивов небольшого размера. Сложность O(n^2)
from random import randint


list_ = []
N = 10

for i in range(N):
    list_.append(randint(0, 99))

print(list_)

for i in range(N-1):
    for j in range(N-1-i):
        if list_[j] > list_[j+1]:
            list_[j], list_[j+1] = list_[j+1], list_[j]

print(list_)
