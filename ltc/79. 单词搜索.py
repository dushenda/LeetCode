#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 79. 单词搜索.py
@author     : CALIBRATION
@time       : 2020/9/11 14:08
@description: None
"""
from typing import List


# answer
class Solution(object):
    # 定义上下左右四个行走方向
    directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def exist(self, board, word):
        m, n = len(board), len(board[0])
        if m == 0: return False
        mark = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    mark[i][j] = 1  # 将该元素标记为已使用
                    if self.backtrack(i, j, mark, board, word[1:]):
                        return True
                    else:
                        mark[i][j] = 0  # 回溯
        return False

    def backtrack(self, i, j, mark, board, word):
        if len(word) == 0: return True
        for direct in self.directs:
            cur_i = i + direct[0]
            cur_j = j + direct[1]
            if 0 <= cur_i < len(board) and 0 <= cur_j < len(board[0]) and board[cur_i][cur_j] == word[0]:
                if mark[cur_i][cur_j] == 1: continue
                mark[cur_i][cur_j] = 1  # 将该元素标记为已使用
                if self.backtrack(cur_i, cur_j, mark, board, word[1:]):
                    return True
                else:
                    mark[cur_i][cur_j] = 0  # 回溯，该节点不满足相等条件，回溯上一节点进行下一方向的尝试
        return False


# wrong
class Solution2:
    directions = [(1, 0), (0, -1), (0, 1), (-1, 0)]

    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        mark = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    mark[i][j] = 1
                    if self.dfs(board, word[1:], i, j, mark):
                        return True
                    else:
                        mark[i][j] = 0
        return False

    def dfs(self, board, word, i, j, mark):
        if len(word) == 0: return True
        for direction in self.directions:
            cur_i, cur_j = i + direction[0], j + direction[1]
            if 0 <= cur_i < len(board) and 0 <= cur_j < len(board[0]) and mark[cur_i][cur_j] != 1 and board[cur_i][
                cur_j] == word[0]:
                mark[cur_i][cur_j] = 1
                if self.dfs(board, word[1:], cur_i, cur_j, mark):
                    return True
                else:
                    mark[cur_i][cur_j] = 0
        return False


def main():
    board = [['A', 'B', 'C', 'E'],
             ['S', 'F', 'C', 'S'],
             ['A', 'D', 'E', 'E']]
    word = "ABCB"
    s = Solution2()
    res = s.exist(board, word)
    print(res)


if __name__ == '__main__':
    main()
    # a = bytearray([1,2,3,4])
    # print(a)
