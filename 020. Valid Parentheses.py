# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine
# if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

class Solution:
    def isValid(self, s: str) -> bool:
        complement = {"(": ")", "{": "}", "[": "]"}
        l = []
        for c in s:
            if c in complement:
                l.append(complement[c])
            else:
                if len(l) == 0 or c != l.pop():
                    return False
        if len(l) == 0:
            return True
        else:
            return False

s = Solution()
assert True == s.isValid("()")
assert True == s.isValid("()[]{}")
assert False == s.isValid("(]")
assert False == s.isValid("([)]")
assert True == s.isValid("{[]}")
assert True == s.isValid("")
assert False == s.isValid("{")
assert False == s.isValid("}")
