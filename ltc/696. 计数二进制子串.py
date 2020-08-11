#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 696. 计数二进制子串.py
@author     : CALIBRATION
@time       : 2020/8/10 16:54
@description: None
"""


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # 超时
        lens = len(s)
        res = 0
        for i in range(lens):
            for j in range(i + 2, lens + 1, 2):
                tmp = [int(i) for i in s[i:j]]
                tmp2 = [a - b for a in tmp[0:len(tmp) // 2] for b in tmp[len(tmp) // 2:]]
                if abs(sum(tmp2)) == len(tmp2):
                    print(tmp)
                    res += 1
        return res

    def countBinarySubstrings2(self, s: str) -> int:
        cnt = []
        tmp_cnt = 1
        tmp_str = s[0]
        for iv in s[1:]:
            if iv == tmp_str:
                tmp_cnt += 1
            else:
                cnt.append(tmp_cnt)
                tmp_str = iv
                tmp_cnt = 1
        cnt.append(tmp_cnt)
        res = 0
        for i in range(1, len(cnt)):
            res += cnt[i - 1] if cnt[i - 1] < cnt[i] else cnt[i]
        return res

    def countBinarySubstrings3(self, s: str) -> int:
        last, tmp_cnt, res = 0, 1, 0
        tmp_str = s[0]
        for iv in s[1:]:
            if iv == tmp_str:
                tmp_cnt += 1
            else:
                res += min(last, tmp_cnt)
                last = tmp_cnt
                tmp_str = iv
                tmp_cnt = 1
        res += min(last, tmp_cnt)
        return res


def main():
    s = Solution()
    input = "00110011"
    res = s.countBinarySubstrings3(input)
    print(res)


if __name__ == '__main__':
    main()
