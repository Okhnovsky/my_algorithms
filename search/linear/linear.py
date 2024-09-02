# Линейный поиск используется для поиска элемента в 
# неотсортированном массиве. Сложность O(n). 
# Вместо предварительной сортировки с дальнейшим бинарным поиском, 
# эффективнее использовать данный алгоритм.
from typing import Optional


def linear_search(array: list[int], value: int) -> Optional[int]:
    """
    Возвращает индекс найденного элемента.
    Если искомый элемент отсутствует, возвращает
    None.
    """
    for index, item in enumerate(array):
        if item == value:
            return index


def input_data() -> tuple:
    array = list(map(int, input().strip().split()))
    value = int(input())
    return array, value


def main() -> None:
    array, value = input_data()
    index = linear_search(array, value)
    print(index)


if __name__ == "__main__":
    main()
