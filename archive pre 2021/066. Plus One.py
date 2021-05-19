# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
#
# The digits are stored such that the most significant digit is at the head of the list,
# and each element in the array contain a single digit.
#
# You may assume the integer does not contain any leading zero, except the number 0 itself.
#
# Example 1:
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.

# Example 2:
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.

from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        d = len(digits)-1
        carry = 1
        while (d >= 0):
            if carry == 1:
                if digits[d] == 9:
                    digits[d] = 0
                    carry = 1
                else:
                    digits[d] += 1
                    carry = 0
            d -= 1
        if carry == 1:
            digits = [1] + digits
        return digits
s = Solution()
assert [1,2,4] == s.plusOne([1,2,3])
assert [4,3,2,2] == s.plusOne([4,3,2,1])
assert [1] == s.plusOne([0])
assert [1,0] == s.plusOne([9])
assert [1,0,0,0] == s.plusOne([9,9,9])
assert [9,8,0] == s.plusOne([9,7,9])
assert [1,0,0,0] == s.plusOne([9,9,9])
