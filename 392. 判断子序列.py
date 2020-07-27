class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s):
            if j == len(t) - 1 or i == len(s) - 1:
                break
            if s[i] == t[j]:
                i += 1
                j += 1
                continue
            j += 1
        if i < len(s) - 1:
            return False
        return True

# Huawei 1
# def gtr(x, y):
#     a, b = x, y
#     while x != 0:
#         x, y = y % x, x
#     return int(a * b / y)
#
#
# import sys
#
# for line in sys.stdin:
#     a = line.split()
#     x, y = int(a[0]), int(a[1])
#     print(gtr(x, y))
