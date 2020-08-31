class Solution:
    def GetCoinCount(self, N):
        n = 1024 - N
        r = n % 64
        res = n // 64

        res += r // 16
        r = r % 16
        res += r // 4
        r = r % 4
        res += r
        return res
