n, m = list(map(int, input().split()))
res = 0
for i in range(1, n + 1):
    for bs in range(1, n + 1):
        if i * bs ** (m - 1) <= n:
            res += 1
        else:
            break
print(res % 998244353)
