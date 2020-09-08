#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 486. 预测赢家.py
@author     : CALIBRATION
@time       : 2020/9/1 16:08
@description: None
"""
from typing import List


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def total(start: int, end: int, turn: int) -> int:
            if start == end: return nums[start] * turn
            scoreStart = nums[start] * turn + total(start + 1, end, -turn)
            scoreEnd = nums[end] * turn + total(start, end - 1, -turn)
            return max(scoreStart * turn, scoreEnd * turn) * turn
        return total(0, len(nums) - 1, 1) >= 0

    def PredictTheWinner2(self, nums: List[int]) -> bool:
        length = len(nums)
        dp = [[0] * length for _ in range(length)]
        for i, num in enumerate(nums):
            dp[i][i] = num
        for i in range(length - 2, -1, -1):
            for j in range(i + 1, length):
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
        return dp[0][length - 1] >= 0


def main():
    pass


if __name__ == '__main__':
    main()
