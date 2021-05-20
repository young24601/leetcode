# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

class Solution:
    def reverse(self, x: int) -> int:
        reversed_string = ""
        if x < 0:
            reversed_string = "-"
        x = abs(x)
        while x // 10 > 0:
            reversed_string += str(x % 10)
            x //= 10
        reversed_string += str(x % 10)
        if (int(reversed_string) > pow(2,31) - 1) or (int(reversed_string) < -pow(2,31)):
            return 0
        return int(reversed_string)


# a more concise solution would be:
    def reverse2(self, x: int) -> int:
        if x < 0:
            a = -1 * int(str(abs(x))[::-1])
        else:
            a = int(str(x)[::-1])
        if abs(a) >= 2**31-1:
            return 0
        return a

s = Solution()
assert 321 == s.reverse(123)
assert -321 == s.reverse(-123)
assert 21 == s.reverse(120)
assert 0 == s.reverse(0)
assert -2 == s.reverse(-2)
assert 21 == s.reverse(1200)
assert -21 == s.reverse(-1200)
assert 1 == s.reverse(10000)
assert 0 == s.reverse(2147483647)
