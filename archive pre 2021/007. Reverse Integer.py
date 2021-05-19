# Given a 32-bit signed integer, reverse digits of an integer.
# 
# Example 1:
# 
# Input: 123
# Output: 321
# Example 2:
# 
# Input: -123
# Output: -321
# Example 3:
# 
# Input: 120
# Output: 21

class Solution:
    def reverse(self, x):
        if x < 0:
            a = -1 * int(str(abs(x))[::-1])
        else:
            a = int(str(x)[::-1])
        if abs(a) >= 2**31-1:
            return 0
        return a
        
        
s = Solution()
s.reverse(123)
s.reverse(-123)
s.reverse(120)
s.reverse(1534236469)

