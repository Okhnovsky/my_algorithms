# Данный алгоритм эффективнее алгоритмов сотрировок
# вставками, выбором и пузырьковой. Сложность алгоритма O(nlogn).
# Для реализации используется структура данных двоичная Куча - Max Heap
# (бинарное дерево), в котором наибольший эдемент - это вершина дерева
from typing import List


def heapify(nums: List[int], heap_size: int, root_index: int) -> List[int]:
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        heapify(nums, heap_size, largest)


def heapsort(nums: List[int]) -> List[int]:
    n = len(nums)

    for i in range(n, -1, -1):
        heapify(nums, n, i)

    for i in range(n-1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)


def main() -> None:
    nums: List[int] = list(map(int, input().strip().split()))
    heapsort(nums)
    print(nums)


if __name__ == "__main__":
    main()
