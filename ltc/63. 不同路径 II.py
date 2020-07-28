class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])  # row:m,col:n
        dp = [[0 for _ in range(n)] for _ in range(m)]  # row:m,col:n
        if obstacleGrid[0][0] == 1:
            return 0
        else:
            dp[0][0] = 1
        for i in range(1, m):  # first col
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i-1][0]
        for i in range(1, n):
            if obstacleGrid[0][i] == 0:
                dp[0][i] = dp[0][i-1]
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1] + dp[i][j]
        return dp[m - 1][n - 1]


if __name__ == '__main__':
    sol = Solution()
    input = [[0, 0], [1, 1], [0, 0]]
    res = sol.uniquePathsWithObstacles(input)
    print(res)
