class Solution:
    def reverseWords(self, s: str) -> str:
        strs = s.split()
        res = []
        for ss in strs:
            res.append(ss[::-1])
        return ' '.join(res)


if __name__ == '__main__':
    s = Solution()
    strs = "Let's take LeetCode contest"
    res = s.reverseWords(strs)
    print(res)
