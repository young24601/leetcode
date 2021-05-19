#12. Integer to Roman

#Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# There are six instances where subtraction is used:
# 
# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.

class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 1 or num > 3999:
            return ""
        
        roman = ""
        while num > 0:
            if num >= 900:
                if num < 1000:
                    roman += "CM"
                    num -= 900
                else:
                    roman += "M"
                    num -= 1000
            elif num >= 400:
                if num < 500:
                    roman += "CD"
                    num -= 400
                else:
                    roman += "D"
                    num -= 500
            elif num >= 90:
                if num < 100:
                    roman += "XC"
                    num -= 90
                else:
                    roman += "C"
                    num -= 100
            elif num >= 40:
                if num < 50:
                    roman += "XL"
                    num -= 40
                else:
                    roman += "L"
                    num -= 50
            elif num >= 9:
                if num == 9:
                    roman += "IX"   
                    num -= 9
                else:
                    roman += "X"
                    num = num - 10
            elif num >= 4:
                if num == 4:
                    roman += "IV"
                    num -= 4
                else:
                    roman += "V"
                    num -= 5
            else:
                roman += "I"
                num -= 1
        
        print(roman)
        return roman

    # solution is kind of lame, try something more pythonic maybe
    # predefine all of the int and roman values.  go through the numbers in decreasing
    # order and add the necessary romans
    def intToRoman2(self, num):
        intvalue = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romanvalue = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        roman = ""
        for i, r in zip(intvalue, romanvalue):
            roman += (num // i) * r
            num %= i
        return roman
                        
s = Solution()
assert s.intToRoman2(0) == ""
assert s.intToRoman2(3) == "III"
assert s.intToRoman2(58) == "LVIII"
assert s.intToRoman2(4) == "IV"
assert s.intToRoman2(9) == "IX"
assert s.intToRoman2(1994) == "MCMXCIV"

print(s.intToRoman2(3999))
print(s.intToRoman2(621))
