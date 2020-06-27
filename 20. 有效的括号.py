import collections


class Solution:
    def isValid(self, s: str) -> bool:
        # '('，')'，'{'，'}'，'['，']'
        dict_pair = {')': '(', '}': '{', ']': '['}
        stack = collections.deque()
        lens = len(s)
        for i in range(lens):
            if s[i] in dict_pair.keys():
                if not len(stack):
                    return False
                else:
                    tmp = stack.pop()
                    if dict_pair[s[i]] != tmp:
                        return False
            else:
                stack.append(s[i])
        if len(stack):
            return False
        return True


if __name__ == '__main__':
    s = Solution()
    input = "["
    res = s.isValid(input)
    print(res)
