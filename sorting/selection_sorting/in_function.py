# Эффективен для массивов небольшого размера. Сложность O(n^2). 
# Быстрее сортировки пузырьком, так как количество перестановок меньше.
from typing import List


def selection(array: List[int]) -> List[int]:
    n = len(array)
    for i in range(n-1):
        minimum = i
        for j in range(i+1, n):
            if array[j] < array[minimum]:
                minimum = j
            array[i], array[minimum] = array[minimum], array[i]
    return array


def input_array() -> List[int]:
    array = list(map(int, input().strip().split()))
    return array


def main() -> None:
    array: List[int] = input_array()
    print(array)
    print(selection(array))


if __name__ == "__main__":
    main()
