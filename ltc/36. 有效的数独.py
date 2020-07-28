#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 36. 有效的数独.py
@author     : CALIBRATION
@time       : 2020/7/9 9:27
@description: None
"""


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        m, n = len(board), len(board[0])  # m:row n:col
        row, col, box = [{} for _ in range(9)], [{} for _ in range(9)], [{} for _ in range(9)]
        for i in range(m):  # i:row j:col
            for j in range(n):
                v = board[i][j]
                if v != '.':
                    box_index = (i // 3) * 3 + j // 3
                    if row[i].get(v, False):
                        return False
                    else:
                        row[i][v] = 1
                    if col[j].get(v, False):
                        return False
                    else:
                        col[j][v] = 1
                    if box[box_index].get(v, False):
                        return False
                    else:
                        box[box_index][v] = 1

        return True


def main():
    input = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    sol = Solution()
    res = sol.isValidSudoku(input)
    print(res)


if __name__ == '__main__':
    main()
