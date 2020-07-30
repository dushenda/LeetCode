#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 1.两数之和.py
@author     : CALIBRATION
@time       : 2020/4/30 11:07
@description: None
"""
import unittest


class Solution(object):
    def twoSum(self, nums, target):
        # 太暴力了，2744ms，13.4MB
        r = range(len(nums))
        for i1 in r:
            another = target - nums[i1]
            for i2 in r:
                if nums[i2] == another and i1 != i2:
                    return [i1, i2]
        return [0, 0]

    def twoSum2(self, nums, target):
        # 36ms，14.4MB
        # 使用字典做哈希,hash同一个值得到的键值是不变的，这里之所以可以得到正确的结果，是因为，第二次访问的是列表，每次必先访问hash被覆盖的那个值
        hash_nums = {}
        for idx, val in enumerate(nums):
            hash_nums[val] = idx
        for i, v in enumerate(nums):
            j = hash_nums.get(target - v)  # dict().get()得不到会返回None,dict()[]得不到就会报异常
            if j is not None and i != j:
                return [i, j]
        return [0, 0]

    def twoSum3(self, nums, target):
        # 异常处理时间太久520ms，13.5MB
        for i, u in enumerate(nums):
            v = target - u
            try:
                j = nums.index(v)
                if j != i:
                    return [i, j]
                else:
                    try:
                        j = nums.index(v, i + 1)
                        return [i, j]
                    except ValueError:
                        continue
            except ValueError:
                continue

    def twoSum4(self, nums, target):
        # 64ms,15.2MB
        hash_nums = {}
        for i, v in enumerate(nums):
            if hash_nums.get(target - v) is not None:
                return [i, hash_nums.get(target - v)]
            hash_nums[v] = i
        return [0, 0]

    def twoSum5(self, nums, target):
        # 1140ms,14.6MB最好别用异常处理，耗时很高
        for i, u in enumerate(nums):
            v = target - u
            if v in nums:
                j = nums.index(v)
                if j == i:
                    try:
                        j = nums.index(v, i + 1)
                    except ValueError:
                        continue
                if j:
                    return [i, j]
            else:
                continue
        return [0, 0]


def main():
    t = unittest.TestCase()
    s = Solution()
    test_input1 = [[3, 3], [2, 7, 11, 15], [1, 7, 5, 9, 0], [3, 2, 4]]
    test_input2 = [6, 9, 16, 6]
    test_output = [[0, 1], [0, 1], [1, 3], [1, 2]]
    for i in range(3):
        t.assertEqual(s.twoSum2(test_input1[i], test_input2[i]), test_output[i])
    for i in range(3):
        t.assertEqual(s.twoSum3(test_input1[i], test_input2[i]), test_output[i])
    for i in range(3):
        t.assertEqual(sorted(s.twoSum4(test_input1[i], test_input2[i])), test_output[i])
    for i in range(3):
        t.assertEqual(sorted(s.twoSum5(test_input1[i], test_input2[i])), test_output[i])


if __name__ == '__main__':
    # main()
    def twoSum(nums, target):
        d = dict()
        for i, iv in enumerate(nums):
            if d.get(target - iv) is not None:
                return [d.get(target - iv), i]
            d[iv] = i


    nums = [2, 11, 7, 15]
    target = 9
    res = twoSum(nums, target)
    print(res)
