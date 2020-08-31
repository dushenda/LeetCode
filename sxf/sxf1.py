#
#
# @param str1 string字符串 原始的字符串
# @param str2 string字符串 转换的字符串
# @return string字符串
#
class Solution:
    def find_diff_char(self, str1, str2):
        l1, l2 = len(str1), len(str2)
        s1 = str1 if l1 > l2 else str2
        s2 = str1 if l1 < l2 else str2
        s1, s2 = sorted(s1), sorted(s2)  # s1>s2
        for i in range(len(s2)):
            if s1[i] != s2[i]:
                return s1[i]
        return s1[-1]


if __name__ == '__main__':
    s1 = "abcde"
    s2 = "abcxde"
    s = Solution()
    res = s.find_diff_char(s1, s2)
    print(res)
