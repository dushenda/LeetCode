#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 8. 字符串转换整数 (atoi).py
@author     : CALIBRATION
@time       : 2020/6/17 10:17
@description: None
"""


class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.lstrip()
        sym_all = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '+']
        sym = ['-', '+']
        if len(str) == 0:
            return 0
        if str[0] not in sym_all:
            return 0
        if len(str) > 2 and str[0] in sym and str[1] in sym:
            return 0
        num = ''
        flag = 1
        if str[0] == '-':
            flag = -1
            str = str.replace('-', '')
        elif str[0] == '+':
            str = str.replace('+', '')
        for c in str:
            if '0' <= c <= '9':
                num += c
            else:
                break
        if num == '':
            res = 0
        else:
            res = int(num)
        if res >= 2147483648:
            if flag == -1:
                return flag * 2147483648
            else:
                return flag * (2147483648 - 1)
        return flag * res


def main():
    str = "-91283472332"
    s = Solution()
    res = s.myAtoi(str)
    print(res)


if __name__ == '__main__':
    main()
