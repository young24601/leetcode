#8. String to Integer (atoi)

# Implement atoi which converts a string to an integer.
# 
# The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. 
# Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible,
# and interprets them as a numerical value.
# 
# The string can contain additional characters after those that form the integral number, which are ignored and have no effect on
# the behavior of this function.
# 
# If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because 
# either str is empty or it contains only whitespace characters, no conversion is performed.
# 
# If no valid conversion could be performed, a zero value is returned.


import re
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        s = re.search('^(([+|-]\d+)|\d+)', str.strip())
        
        if s is None:
            return 0
        else:
            if int(s.group()) > 2**31-1:
                return 2**31-1
            elif int(s.group()) < -2**31:
                return -2**31
            else:
                return int(s.group())


s = Solution()
s.myAtoi("42")
s.myAtoi("   -42")
s.myAtoi("4193 with words")
s.myAtoi("words and 987")
s.myAtoi("-91283472332")
s.myAtoi("0000091283472332")
s.myAtoi("0-1")
s.myAtoi("+-2")
s.myAtoi("-91283472332")