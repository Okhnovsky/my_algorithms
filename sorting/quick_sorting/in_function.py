# Сложность O(n log n) - если опорный элемент в середине.
# Если опорный элемент max or min - О(n^2).


def quicksort(arr):
    if len(arr) <= 0:
        return arr
    middle_element_index = len(arr) // 2
    pivot = arr[middle_element_index]
    left, center, right = partition(arr, pivot)

    return quicksort(left) + center + quicksort(right)


def partition(arr, pivot):
    left, center, right = [], [], []
    for item in arr:
        if item < pivot:
            left.append(item)
        if item > pivot:
            right.append(item)
        if item == pivot:
            center.append(item)
    return left, center, right


def main():
    random_list_of_nums = list(map(int, input().strip().split()))
    quicksort(random_list_of_nums)
    print(quicksort(random_list_of_nums))


if __name__ == "__main__":
    main()
