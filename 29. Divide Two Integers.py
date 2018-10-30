#29. Divide Two Integers
# Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

# Return the quotient after dividing dividend by divisor.

# The integer division should truncate toward zero.


class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # naive subtraction solution was way too slow, so try to implement
        # bitwise operations to solve the problem.

        # recall that x << y shifts x to the left y places (same as multiplying x by 2**y)
        # recall that x >> y shifts x to the right y places (same as dividing x by 2**y)

        print






s = Solution()

assert s.divide(10, 3) == 3
assert s.divide(7, -3) == -2
assert s.divide(-10, -3) == 3
assert s.divide(-7, 3) == -2
assert s.divide(1, 1) == 1
assert s.divide(0, 1) == 0
assert s.divide(-2147483648, -1) == 0


#         ct = 0
#         if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
#             pos = True
#         else:
#             pos = False
#         while abs(dividend) >= abs(divisor):
#             dividend = abs(dividend) - abs(divisor)
#             ct += 1
#
#         if pos:
#             return ct
#         else:
#             return -ct
