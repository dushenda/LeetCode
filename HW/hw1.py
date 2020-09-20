from typing import List


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    if not matrix: return []
    m, n = len(matrix), len(matrix[0])
    t, b, l, r = 0, m - 1, 0, n - 1
    res = []
    while True:
        for i in range(l, r + 1):
            res.append(matrix[t][i])
        if t < b:
            t += 1
        else:
            break
        for i in range(t, b + 1):
            res.append(matrix[i][r])
        if r > l:
            r -= 1
        else:
            break
        for i in range(r, l - 1, -1):
            res.append(matrix[b][i])
        if b > t:
            b -= 1
        else:
            break
        for i in range(b, t - 1, -1):
            res.append(matrix[i][l])
        if l < r:
            l += 1
        else:
            break
    return res
