class Solution:
    def IsValidExp(self, s):
        if len(s) == 1:
            return False
        stack = []
        left = ['(', '[', '{']
        right = [')', ']', '}']
        dic = {')': '(', ']': '[', '}': '{'}
        for i in range(len(s)):
            if s[i] in left:
                stack.append(s[i])
            if s[i] in right:
                tmp = stack.pop()
                if dic[s[i]] == tmp:
                    continue
                else:
                    return False
        return True
