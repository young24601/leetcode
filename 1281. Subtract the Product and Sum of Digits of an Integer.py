# Given an integer number n, return the difference between the product of its digits and the sum of its digits.



class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum = 0
        for digit in str(n):
            product *= int(digit)
            sum += int(digit)
        return product - sum



s = Solution()
assert 15 == s.subtractProductAndSum(234)
assert 21 == s.subtractProductAndSum(4421)
