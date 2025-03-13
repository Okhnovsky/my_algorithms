# Эффективен для массивов небольшого размера. Сложность O(n^2). 
# Быстрее сортировки пузырьком, так как количество перестановок меньше.
from random import randint


N = 10
array = []

for i in range(N):
    array.append(randint(1, 99))

print(array)
for i in range(N-1):
    minimum = i
    for j in range(i+1, N):
        if array[j] < array[minimum]:
            array[j], array[minimum] = array[minimum], array[j]

print(array)
