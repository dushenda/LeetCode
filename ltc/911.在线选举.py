#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 911.在线选举.py
@author     : CALIBRATION
@time       : 2020/6/13 14:34
@description: None
"""
import bisect


class TopVotedCandidate:

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        l = len(times)
        self.t = times
        self.winner = [persons[0]] * l
        d = dict()
        winner_bynow = persons[0]
        max_ticket = 1
        d[persons[0]] = 1
        for i in range(1, l):
            if persons[i] in d:
                d[persons[i]] += 1
            else:
                d[persons[i]] = 1
            if d[persons[i]] >= max_ticket:
                winner_bynow = persons[i]
                max_ticket = d[persons[i]]
            self.winner[i] = winner_bynow

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        index = bisect.bisect(self.t, t) - 1
        return self.winner[index]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)

def main():
    s = TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30])
    q = [3, 12, 25, 15, 24, 8]
    for i in q:
        res = s.q(i)
        print(res)


if __name__ == '__main__':
    main()
