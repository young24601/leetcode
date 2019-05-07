"""Implement pow(x, n), which calculates x raised to the power n (x^n).

Example 1:
Input: 2.00000, 10
Output: 1024.00000

Example 2:
Input: 2.10000, 3
Output: 9.26100

Example 3:
Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−2^31, 2^31 − 1]"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            return 1 / self.myPow(x, -n)

        if n % 2:
            print("a1: " + str(x) + " * myPow(" + str(x*x) + ", " + str(n//2) + ")")
            return x * self.myPow(x*x, n//2)
            # else:
            #     print("a2 (" + (str(x)) + "," + str(n) + "): " + str(1/x) + " * myPow(" + str(x) + ", " + str(-(-n//2)) + ") ^ 2")
            #     return 1/x * self.myPow(x*x, -(-n//2))

        return self.myPow(x*x, n//2)

s = Solution()
output = s.myPow(2, -4)
#output = s.myPow(0.00001, 2147483647)
print(output)

#0.00001
#2147483647
