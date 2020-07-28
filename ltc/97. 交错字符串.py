class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str):
        if len(s1) + len(s2) != len(s3):
            return False
        if not s1:
            return s2 == s3
        if not s2:
            return s1 == s3
        s1, s2, s3 = '0' + s1, '0' + s2, '0' + s3
        m, n = len(s1), len(s2)  # s1 row and s2 col
        dp = [[False for _ in range(n)] for _ in range(m)]  # m row and n col
        dp[0][0] = True
        for i in range(1, n):
            dp[0][i] = dp[0][i - 1] and (s2[i] == s3[i])
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] and (s1[i] == s3[i])
        for i in range(1, m):
            for j in range(1, n):
                if dp[i][j - 1]:
                    dp[i][j] = s2[j] == s3[i + j]
                if dp[i - 1][j]:
                    dp[i][j] = s1[i] == s3[i + j]
                else:
                    continue
        return dp[m - 1][n - 1]


if __name__ == '__main__':
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    # s1 = "aabaac"
    # s2 = "aadaaeaaf"
    # s3 = "aadaaeaabaafaac"
    sol = Solution()
    res = sol.isInterleave(s1, s2, s3)
    print(res)
