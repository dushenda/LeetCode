def binary_search(nums: list, target: int, begin: int, end: int) -> int:
    if begin >= end:
        if nums[begin] == target:
            return begin
        else:
            return -1
    else:
        m = (begin + end) // 2
        if target <= nums[m]:
            end = m
            return binary_search(nums, target, begin, end)
        else:
            begin = m + 1
            return binary_search(nums, target, begin, end)


import math


def fib(n):
    sqrt5 = math.sqrt(5)
    res = 1 / sqrt5 * ((1 + sqrt5) ** n - (1 - sqrt5) ** n) / 2 ** n
    return int(res)


if __name__ == '__main__':
    # input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 99]
    # target = 99
    # res = binary_search(input, target, 0, len(input) - 1)
    # print(res)
    n = 100
    res = fib(n)
    print(res)
