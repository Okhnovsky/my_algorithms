# Эффективен для массивов небольшого размера. Сложность O(n^2). 
# Быстрее сортировки пузырьком, так как количество перестановок меньше.
# Если массив частично отсортирован, то алгоритм эффективнее сортировки выбором.
from typing import List


def insertion(array: List[int]) -> List[int]:
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i - 1

        while j >= 0 and array[j] > item_to_insert:
            array[j+1] = array[j]
            j -= 1

        array[j+1] = item_to_insert
    
    return array


def get_array() -> List[int]:
    array = list(map(int, input().strip().split()))
    return array


def main() -> None:
    array = get_array()
    print(array)
    sorted_array = insertion(array)
    print(sorted_array)


if __name__ == "__main__":
    main()
