#
#
# @param chars string字符串一维数组
# @return string字符串
#
from collections import Counter


class Solution:
    def commonChars(self, chars):
        ans = Counter(chars[0])
        for i in chars[1:]:
            ans &= Counter(i)
        return "".join(sorted(ans.elements()))


if __name__ == '__main__':
    s = Solution()
    a = ["bella", "label", "roller"]
    res = s.commonChars(a)
    print(res)
