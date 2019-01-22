#20. Valid Parentheses

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        opposite = {'(':')', '{':'}', '[':']'}
        for c in s:
            if c in opposite:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                else:
                    out = stack.pop()
                if c != opposite[out]:
                    return False

        if len(stack) > 0:
            return False
        return True

s = Solution()
print(s.isValid(""))
print(s.isValid("()"))
print(s.isValid("()[]{}"))
print(s.isValid("(]"))
print(s.isValid("([)]"))
print(s.isValid("{[]}"))
print(s.isValid("]"))
