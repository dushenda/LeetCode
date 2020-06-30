from collections import Counter


class Solution:
    # def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
    def canMakePaliQueries(self, s, queries):
        # 超时
        res = []
        for left, right, k in queries:
            if k >= 13:# 这个挺不错的
                res.append(True)
            else:
                sub_list = s[left:right + 1]  # 得到子串
                dic = Counter(sub_list)
                cnt = sum([i % 2 for i in dic.values()])
                if len(sub_list) % 2 == 0:
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


if __name__ == '__main__':
    s = Solution()
    ss = "abcda"
    queries = [[3, 3, 0], [1, 2, 0], [0, 3, 1], [0, 3, 2], [0, 4, 1]]
    res = s.canMakePaliQueries(ss, queries)
    print(res)
