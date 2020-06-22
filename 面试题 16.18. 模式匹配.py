#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeeCode
@file       : 面试题 16.18. 模式匹配.py
@author     : CALIBRATION
@time       : 2020/6/22 11:31
@description: None
"""
from collections import Counter


class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        """
        a_cnt     # pattern 里面 a 的数量
        a         # a 匹配的字符串
        a_l       # a 匹配字符串的长度
        a_max_l   # a 可能匹配字符串的最大长度，用来穷举 a_l，应该有的a的长度
        """
        ca, cb = pattern.count('a'), pattern.count('b')
        if ca < cb:
            ca, cb = cb, ca
            pattern = ''.join('a' if ch == 'b' else 'b' for ch in pattern)

        if not value:
            return cb == 0
        if not pattern:
            return False

        for la in range(len(value) // ca + 1):
            # la 代表a的长度
            rest = len(value) - la * ca  # =lb*cb?
            if (cb == 0 and rest == 0) or (cb != 0 and rest % cb == 0):
                lb = 0 if cb == 0 else rest // cb
                pos, cor = 0, True
                a_value, b_value = None, None
                # 遍历pattern看是否匹配
                for ch in pattern:
                    if ch == 'a':
                        sub = value[pos:pos + la]
                        if not a_value:
                            a_value = sub
                        else:
                            if a_value != sub:
                                cor = False
                                break
                        pos += la
                    else:
                        sub = value[pos:pos + lb]
                        if not b_value:
                            b_value = sub
                        else:
                            if b_value != sub:
                                cor = False
                                break
                        pos += lb
                if cor and a_value != b_value:
                    return True
        return False


def main():
    s = Solution()
    pattern = "abba"
    value = "dogcatcatdog"
    res = s.patternMatching(pattern, value)
    print(res)


if __name__ == '__main__':
    main()
