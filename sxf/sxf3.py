#
#
# @param nums int整型一维数组
# @param m int整型
# @return int整型
#
class Solution:
    def min_send(self, nums, m):
        def check(x):
            t, cnt = 0, 1
            for num in nums:
                if t + num > x:
                    cnt += 1
                    t = num
                else:
                    t += num
            return cnt <= m

        l, r = max(nums), sum(nums)
        while l < r:
            mid = l + (r - l) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l
        # n = len(nums)
        # f = [[10 ** 18] * (m + 1) for _ in range(n + 1)]
        # sub = [0]
        # for elem in nums:
        #     sub.append(sub[-1] + elem)
        # f[0][0] = 0
        # for i in range(1, n + 1):
        #     for j in range(1, min(i, m) + 1):
        #         for k in range(i):
        #             f[i][j] = min(f[i][j], max(f[k][j - 1], sub[i] - sub[k]))
        # return f[n][m]
