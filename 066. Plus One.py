# Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
# You may assume the integer does not contain any leading zero, except the number 0 itself.

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        add_one = 1
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] + carry + add_one == 10:
                digits[i] = 0
                carry = 1
                if i == 0:
                    return [1] + digits
            else:
                digits[i] += carry + add_one
                return digits
            add_one = 0
        return digits


s = Solution()

assert [1,2,4] == s.plusOne([1,2,3])
assert [9,9,0] == s.plusOne([9,8,9])
assert [4,3,2,2] == s.plusOne([4,3,2,1])
assert [1] == s.plusOne([0])
assert [1,0,0,0] == s.plusOne([9,9,9])
