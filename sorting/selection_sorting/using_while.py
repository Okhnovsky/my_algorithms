# Эффективен для массивов небольшого размера. Сложность O(n^2).
# Быстрее сортировки пузырьком, так как количество перестановок меньше.
from random import randint


N = 10
array = []


for i in range(N):
    array.append(randint(1, 99))

print(array)

i = 0

while i < N-1:
    minimum = i
    j = i + 1
    while j < N:
        if array[j] < array[minimum]:
            minimum = j
        j += 1

    array[i], array[minimum] = array[minimum], array[i]
    i += 1

print(array)
