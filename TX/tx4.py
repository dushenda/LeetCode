def lis(nums):
    n = len(nums)
    m = [0] * n
    res = 0
    for x in range(n - 2, -1, -1):
        for y in range(n - 1, x, -1):
            if nums[x] < nums[y] and m[x] <= m[y]:
                m[x] += 1
        max_value = max(m)
        res = 0
        for i in range(n):
            if m[i] == max_value:
                res += 1
                max_value -= 1
    return res


T = int(input())
for i in range(T):
    n = int(input())
    nums = list(map(int, input().split()))
    res = max(lis(nums), lis(nums[::-1]))
    print(res)
