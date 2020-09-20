n = int(input())
depth = list(map(int, input().split()))
M = 10 ** 9 + 7


def combination(n, k):
    if k == 0 or k == n: return 1
    k = min(k, n - k)
    top = 1
    for i in range(n, n - k, -1): top *= i
    down = 1
    for i in range(1, k + 1): down *= i
    return (top // down) % M


def helper():
    if n == 0: return 0
    max_depth = max(depth)
    depth_count = [0] * (max_depth + 1)
    for d in depth:
        depth_count[d] += 1
    for i in range(max_depth):
        if 2 * depth_count[i] < depth_count[i + 1]:
            return 0

    r = 1
    for i in range(1, max_depth + 1):
        r *= combination(2 * depth_count[i - 1], depth_count[i])
    r %= M
    return r


print(helper())
