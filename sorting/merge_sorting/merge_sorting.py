# Временная сложность О(n logn), пространственная сложность - О(n).
# Алгоритм сортировки устойчивый.
from random import randint


def merge(arr):
    if len(arr) <= 1:
        return arr
    left = merge(arr[0: len(arr) // 2])
    right = merge(arr[len(arr)//2: len(arr)])
    return merge_arr(left, right)


def merge_arr(left, right):
    result = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    return result + left[left_idx:] + right[right_idx:]


if __name__ == "__main__":
    N = 10
    test_array = []
    for _ in range(N):
        test_array.append(randint(1, 99))
    print(merge(test_array))
