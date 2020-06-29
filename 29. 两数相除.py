#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeeCode
@file       : 29. 两数相除.py
@author     : CALIBRATION
@time       : 2020/6/29 19:58
@description: None
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = (dividend > 0) ^ (divisor > 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        count = 0
        # 把除数不断左移，直到它大于被除数
        while dividend >= divisor:
            count += 1
            divisor <<= 1
        result = 0
        while count > 0:
            count -= 1
            divisor >>= 1
            if divisor <= dividend:
                result += 1 << count  # 这里的移位运算是把二进制（第count+1位上的1）转换为十进制
                dividend -= divisor
        if sign: result = -result
        return result if -(1 << 31) <= result <= (1 << 31) - 1 else (1 << 31) - 1

    def divide2(self, dividend: int, divisor: int) -> int:
        limit = 2 ** 31
        is_neg = (dividend < 0) ^ (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        div, track = divisor, 1
        while dividend >= divisor:
            while dividend >= (div << 1):
                div <<= 1
                track <<= 1
            res += track
            dividend -= div
            div, track = divisor, 1
        return max(-limit, min(limit - 1, -res if is_neg else res))

    def divide3(self, dividend: int, divisor: int) -> int:
        pass
        #递归


def main():
    dividend = 7
    divisor = -3
    s = Solution()
    res = s.divide(dividend, divisor)
    print(res)


if __name__ == '__main__':
    main()
