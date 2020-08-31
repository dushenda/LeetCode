n, a, b = list(map(int, input().split()))
A, B = [], []
for i in range(n):
    tmp = list(map(int, input().split()))
    A.append(tmp[0])
    B.append(tmp[1])
res = 0
for i in range(n + 1):
    ia, ib = i, n - i
    tmp_a, tmp_b = [], []
    if ia >= a:
        tmp_a = [i for i in A if i <= ia]
    if ib >= b:
        tmp_b = [i for i in B if i <= ib]
    res = max(sum(tmp_a) + sum(tmp_b), res)

print(res)
