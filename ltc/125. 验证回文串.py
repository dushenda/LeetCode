#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 125. 验证回文串.py
@author     : CALIBRATION
@time       : 2020/8/6 19:38
@description: None
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 去掉空格和逗号
        # 提前upper()
        s_use = [i.upper() for i in s if ('A' <= i <= 'Z') or ('0' <= i <= '9') or ('a' <= i <= 'z')]# O(n)
        for i in range(len(s_use) // 2):# O(n/2)
            # 大小写
            if s_use[i] != s_use[len(s_use) - i - 1]:
                return False
        return True

# O(n)+O(n/2)=O(n)

def main():
    input = "ab_a"
    s = Solution()
    res = s.isPalindrome(input)
    print(res)


if __name__ == '__main__':
    # a = "1abc"
    # print(a.upper())
    # main()
    # s = "abc de,:Af"
    # s_use = [i for i in s if i >= 'A' and i <= 'z']
    # print(s_use)
    print(int(0.6))
