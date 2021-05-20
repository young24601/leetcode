# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII,
# which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right. However, the numeral
# for four is not IIII. Instead, the number four is written as IV. Because the one is before the
# five we subtract it making four. The same principle applies to the number nine, which is written as IX.
# There are six instances where subtraction is used:
#
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

class Solution:
    def romanToInt(self, s: str) -> int:
        # strategy here is to "go backward" adding values unless a "valid previous character" is there
        # then you subtract.
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        valid_subtractions = {'I': None, 'V': 'I', 'X': 'I', 'L': 'X', 'C': 'X', 'D': 'C', 'M': 'C'}
        sum = 0
        prev = None
        for c in s[::-1]:
            if prev and c == valid_subtractions[prev]:
                sum -= values[c]
            else:
                sum += values[c]
            prev = c
        return sum

s = Solution()
assert 3 == s.romanToInt("III")
assert 4 == s.romanToInt("IV")
assert 9 == s.romanToInt("IX")
assert 58 == s.romanToInt("LVIII")
assert 49 == s.romanToInt("XLIX")
assert 88 == s.romanToInt("LXXXVIII")
assert 99 == s.romanToInt("XCIX")
assert 999 == s.romanToInt("CMXCIX")
assert 1994 == s.romanToInt("MCMXCIV")
