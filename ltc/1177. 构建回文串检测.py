from collections import Counter


class Solution:
    # def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
    def canMakePaliQueries(self, s, queries):
        # dp1成功了~~~
        res = []
        dp_cnt = [[0 for _ in range(26)] for _ in range(len(s) + 1)]
        for i, si in enumerate(s):
            dp_cnt[i + 1] = [j for j in dp_cnt[i]]
            dp_cnt[i + 1][ord(si) - ord('a')] += 1
        for left, right, k in queries:
            if k >= 13:  # 这个挺不错的
                res.append(True)
            else:
                cnt_list = [(dp_cnt[right + 1][i] - dp_cnt[left][i]) % 2 for i in range(26)]
                cnt = sum(cnt_list)
                if (right - left + 1) % 2 == 0:
                    res.append(cnt <= 2 * k)
                else:
                    res.append(cnt <= 2 * k + 1)
        return res

    def canMakePaliQueries2(self, s, queries):
        # dp
        ans = [True] * len(queries)
        dp = [0] * (len(s) + 1)
        for i in range(1, len(dp)):
            t = dp[i - 1]
            dp[i] = t ^ (1 << (ord(s[i - 1]) - ord('a')))
        for i, (l, r, k) in enumerate(queries):
            if k < 13:
                c1 = dp[r + 1] ^ dp[l]
                c1 = str(bin(c1))
                c1 = Counter(c1)['1']
                ans[i] = k >= (c1 // 2)
        return ans

    def canMakePaliQueries3(self, s, queries):
        # 奇怪解法
        cnt = [0]
        for i, v in enumerate(s):
            cnt.append(cnt[i] ^ 1 << (ord(v) - 97))
        return [bin(cnt[i] ^ cnt[j + 1]).count('1') // 2 <= k for i, j, k in queries]


if __name__ == '__main__':
    s = Solution()
    ss = "abcda"
    queries = [[3, 3, 0], [1, 2, 0], [0, 3, 1], [0, 3, 2], [0, 4, 1]]
    res = s.canMakePaliQueries(ss, queries)
    print(res)
