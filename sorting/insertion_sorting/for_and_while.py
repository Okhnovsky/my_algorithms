# Эффективен для массивов небольшого размера. Сложность O(n^2). 
# Быстрее сортировки пузырьком, так как количество перестановок меньше.
# Если массив частично отсортирован, то алгоритм эффективнее сортировки выбором.
from random import randint


N = 10
array = []

for _ in range(N):
    array.append(randint(1, 99))

print(array)
for i in range(1, N):
    item_to_insert = array[i]
    j = i - 1

    while j >= 0 and array[j] > item_to_insert:
        array[j+1] = array[j]
        j -= 1

    array[j+1] = item_to_insert

print(array)
