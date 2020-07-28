class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        n, m = len(dungeon), len(dungeon[0])
        MAX_VALUE = 10 ** 9
        dp = [[MAX_VALUE] * (m + 1) for _ in range(n + 1)]
        dp[n - 1][m] = dp[n][m - 1] = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                minn = min(dp[i + 1][j], dp[i][j + 1])
                dp[i][j] = max(minn - dungeon[i][j], 1)
        return dp[0][0]


if __name__ == '__main__':
    input = [[-2, - 3, 3],
             [-5, - 10, 1],
             [10, 30, - 5]]
    sol = Solution()
    res = sol.calculateMinimumHP(input)
    print(res)
