# m, n = list(map(int, input().split()))
# left, right, top, bottom = 0, n - 1, 0, m - 1
# while left <= right and top <= bottom:
#     for i in range(left, right + 1):

# def print_matrix(matrix):
#     if not matrix or len(matrix) <= 0 or len(matrix[0]) <= 0:
#         return
#     start = 0
#     rows = len(matrix)
#     columns = len(matrix[0])
#     res = []
#     while columns > start * 2 and rows > start * 2:
#         print_matrix_circle(matrix, columns, rows, start, res)
#         start += 1
#
#
# def print_matrix_circle(matrix, columns, rows, start, res):
#     endX = columns - 1 - start
#     endY = rows - 1 - start
#
#     for i in range(start + 1, endX):
#         res.append(matrix[start][i])
#
#     if start < endY:
#         for i in range(start + 1, endY + 1):
#             res.append(matrix[i][endX])
#
#     if start < endX and start < endY:
#         for i in range(endX - 1, start - 1, -1):
#             res.append(matrix[endY][i])
#
#     if start < endX and start < endY - 1:
#         for i in range(endY - 1, start, -1):
#             res.append(matrix[i][start])

# def foo(matrix):
#     return matrix and list(matrix.pop(0)) + foo(zip(*matrix)[::-1])
#
#
# matrixs = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
# res = foo(matrixs)
# print(res)
