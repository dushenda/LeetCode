class Solution:
    def memoized_cut_rod(self, p, n):
        r = [float("-inf") for i in range(n)]
        return self.memoized_cut_rod_aux(p, n, r)

    def memoized_cut_rod_aux(self, p, n, r):
        if r[n] > 0:
            return r[n]
        if n == 0:
            q = 0
        else:
            q = float("-inf")
            for i in range(1, n):
                q = max(q, p[i] + self.memoized_cut_rod_aux(p, n - i, r))
        r[n] = q
        return q


def main():
    p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    n = 7
    s = Solution()
    res = s.memoized_cut_rod(p, n)
    print(res)


if __name__ == '__main__':
    main()