#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 32. 最长有效括号.py
@author     : CALIBRATION
@time       : 2020/7/4 19:55
@description: None
"""
import collections


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack_sym = collections.deque()
        stack_num = collections.deque()
        not_valid = [0 for _ in s]
        for i, sym in enumerate(s):
            if sym == ")" and len(stack_num) > 0:
                top = stack_sym.pop()
                if top == "(":
                    stack_num.pop()
                    continue
            stack_num.append(i)
            stack_sym.append(sym)
        while len(stack_num) > 0:
            tmp = stack_num.pop()
            not_valid[tmp] = 1
        # 找最长的连续的0
        max_len = 0
        tmp_len = 0
        for i in not_valid:
            if i == 0:
                tmp_len += 1
            else:
                tmp_len = 0
            max_len = tmp_len if tmp_len > max_len else max_len
        return max_len


def main():
    test = ")()())"
    sol = Solution()
    res = sol.longestValidParentheses(test)
    print(res)


if __name__ == '__main__':
    main()
