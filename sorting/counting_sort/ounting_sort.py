# Временная сложность O(n+r). По памяти O(r). Устойчивая. Реализация от 0.


def counting_sort(array, maximum):
    count = [0] * (maximum + 1)

    for item in array:
        count[item] += 1

    sorted_array = []
    for item in range(maximum + 1):
        sorted_array += [item] * count[item]

    return sorted_array


arr = [8, 1, 4, 10, 4, 1, 4, 7, 6, 8, 6, 4, 5, 10, 1, 0, 5, 4, 9, 7]
result = counting_sort(arr, 10)
print(result)
