from typing import List


def func(nums: List[int]):
    nums.sort()
    lens = len(nums)
    res = 10 ** 10
    for i in range(lens):
        for j in range(i + 1, lens):
            new_nums = nums[i:j]
            if separate(new_nums):
                tmp = sum(nums) - sum(new_nums)
                res = tmp if tmp < res else res
    return res


def separate(sub_nums):
    # 子数组不能划分一半
    if sum(sub_nums) % 2:
        return False
    # 子数组划分一半
    target = sum(sub_nums) / 2
    lens = len(sub_nums)
    for i in range(lens):
        for j in range(i + 1, lens):
            if sum(sub_nums[i:j]) == target:
                return True
    return False


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        li = list(map(int, input().split()))
        res = func(li)
        print(res)
