#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 面试题 17.13. 恢复空格.py
@author     : CALIBRATION
@time       : 2020/7/9 9:13
@description: None
"""


class Solution(object):
    def respace(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: int
        """
        n = len(sentence)
        dp = [0 for _ in range(n + 1)]
        for i in range(n):
            dp[i + 1] = dp[i] + 1
            for x in dictionary:
                if len(x) <= i + 1:
                    if x == sentence[i + 1 - len(x):i + 2]:
                        dp[i + 1] = min(dp[i + 1], dp[i + 1 - len(x)])
        return dp[n]


def main():
    pass


if __name__ == '__main__':
    main()
