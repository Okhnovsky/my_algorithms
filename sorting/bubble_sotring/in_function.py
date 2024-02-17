# Эффективен для массивов небольшого размера. Сложность O(n^2)
from random import randint
from typing import List


def bubble(array: List[int]) -> List[int]:
    N = len(array)
    for i in range(N-1):
        for j in range(N-1-i):
            if array[j] > array[j+1]:
                buff = array[j]
                array[j] = array[j+1]
                array[j+1] = buff
    return array


def main() -> None:
    array = []
    for i in range(10):
        array.append(randint(1, 99))
    print(array)
    print(bubble(array))


if __name__ == "__main__":
    main()
