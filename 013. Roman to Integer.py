#13. Roman to Integer
#Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        #use similar strategy to #12
        romanvalues = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        intvalues = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        index = 0
        output = 0
        ct = 0
        while index < len(s):
            r = romanvalues[ct]
            i = intvalues[ct]
            if len(r) == 1 and r == s[index]:
               output += i
               index += 1
            elif len(r) == 2 and index < len(s)-1 and r == s[index] + s[index+1]:
                output += i
                index += 2
            else:
                ct += 1
        return output
        


s = Solution()
assert s.romanToInt("III") == 3
assert s.romanToInt("IV") == 4
assert s.romanToInt("IX") == 9
assert s.romanToInt("LVIII") == 58
assert s.romanToInt("MCMXCIV") == 1994
assert s.romanToInt("MMMCMXCIX") == 3999
assert s.romanToInt("DCXXI") == 621
