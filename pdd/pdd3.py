N, M, T = list(map(int, input().split()))
if T == 0:
    print(0)
else:
    xi, yi, xj, yj = [], [], [], []
    for _ in range(N):
        p, t = list(map(int, input().split()))
        xi.append(p)
        yi.append(t)
    for _ in range(M):
        p, t = list(map(int, input().split()))
        xj.append(p)
        yj.append(t)
    m, n = len(yi), len(yj)

    min_p = 10 ** 10
    for i in range(m):
        if yi[i] >= T:
            min_p = xi[i] if xi[i] < min_p else min_p
    for i in range(n):
        if yj[i] >= T:
            min_p = xj[i] if xj[i] < min_p else min_p
    for i in range(m):
        for j in range(n):
            if yi[i] + yj[j] >= T:
                min_p = xi[i] + xj[j] if xi[i] + xj[j] < min_p else min_p
    if min_p == 10 ** 10:
        min_p = -1
    print(min_p)
