
def binary_search(nums, value, left, right):
    if left > right:
        return

    index = (left + right) // 2
    if value == nums[index]:
        return index
    if value > nums[index]:
        binary_search(nums, value, left=index+1, right=right)
    else:
        binary_search(nums, value, left=left, right=index-1)


def input_data():
    nums = list(map(int, input().strip().split()))
    value = int(input())
    return nums, value


def main():
    nums, value = input_data()
    index = binary_search(nums, value, left=0, right=(len(nums)-1))
    print(index)


if __name__ == "__main__":
    main()
