# Бинарный поиск используется для поиска элемента
# в отсортированном массиве. Сложность алгоритма O(logn).
from typing import Optional


# Второй вариант
def binary_search_second(array: list[int], value: int) -> Optional[int]:
    """
    Производит бинарный поиск элемента и возвращает его индекс, 
    либо None (если значение не найдено).
    """
    left = 0
    # Правая граница определяется таким образом
    right = len(array)

    # Здесь вместо <=, просто <
    while left < right:
        mid = (left + right) // 2

        if array[mid] == value:
            return mid
        # При переопределении границ не добавляем/убавляем 1
        if array[mid] > value:
            right = mid
        if array[mid] < value:
            left = mid


def binary_search(array: list[int], value: int) -> Optional[int]:
    """
    Производит бинарный поиск элемента и возвращает его индекс, 
    либо None (если значение не найдено).
    """
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        
        if array[mid] == value:
            return mid
        if array[mid] > value:
            right = mid - 1
        if array[mid] < value:
            left = mid + 1


def input_data() -> tuple:
    array = list(map(int, input().strip().split()))
    value = int(input())
    return array, value


def main():
    data = input_data()
    index = binary_search(*data)
    print(index)


if __name__ == "__main__":
    main()
