#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : BFS.py
@author     : CALIBRATION
@time       : 2020/7/11 12:45
@description: None
"""


def bfs(g, s, discovered):
    level = [s]
    while len(level) > 0:
        next_level = []
        for u in level:
            for e in g.incident_edges(u):
                v = e.opposite(u)
                if v not in discovered:
                    discovered[v] = e
                    next_level.append(v)
            level = next_level


def bfs2(graph, s):
    deque = [s]
    discovered = set()
    discovered.add(s)
    while len(deque) > 0:
        vertex = deque.pop(0)
        near_node = graph[vertex]
        for w in near_node:
            if w not in discovered:
                discovered.add(w)
                deque.append(w)
        print(vertex)
    return pre


def dfs2(graph: dict, s, discovered: set) -> None:
    # 递归
    if s not in discovered:
        discovered.add(s)
        print(s)
        for vertex in graph[s]:
            dfs2(graph, vertex, discovered)
    else:
        return


def dfs3(graph: dict, s):
    # 栈
    stack = [s]
    discovered = set(s)
    parent = {s: None}
    while len(stack) > 0:
        vertex = stack.pop()
        for w in graph[vertex]:
            if w not in discovered:
                discovered.add(w)
                stack.append(w)
                parent[w] = vertex
        print(vertex)
    return parent


def main():
    graph = {
        "A": ["B", "C"],
        "B": ["A", "C", "D"],
        "C": ["A", "B", "D", "E"],
        "D": ["F", "B", "E", "C"],
        "E": ["D", "C"],
        "F": ["D"]
    }
    # bfs2(graph, "A")
    dis = set()
    res = dfs3(graph, "E")
    for key in res:
        print(key, "===", res[key])


if __name__ == '__main__':
    main()
