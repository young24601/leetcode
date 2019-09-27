# A peak element is an element that is greater than its neighbors.

# Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

# You may imagine that nums[-1] = nums[n] = -inf

# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.

# Input: nums = [1,2,1,3,5,6,4]
# Output: 1 or 5
# Explanation: Your function can return either index number 1 where the peak element is 2,
#              or index number 5 where the peak element is 6.

# Your solution should be in logarithmic complexity.

from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return self.findPeakElementHelper(nums, 0, len(nums) - 1)

    # strategy here is: find the middle.  If the value of the middle is > middle+1
    # (middle + 1 is guaranteed to exist since if there are an odd number of elements in
    # num, it will be between two, and if it is even, it's the left one) then recurse to the right
    # because it means that it is rising to that side and therefore has a peak.  Otherwise recurse to
    # the left.
    # In the case of one remaining element, we know that it has to be a peak.  Note this will not find all peaks
    def findPeakElementHelper(self, nums, left, right):
        if left == right:
            return left
        middle = left + (right - left) // 2  # find middle of left and right then add left which is the beginning of nums we care about

        if nums[middle] > nums[middle+1]:  # mid+1 is safe because mid is either surrounded by two values or in even numbers middle is in the left
            # if this is true, then check to the left
            return self.findPeakElementHelper(nums, left, middle)
        else:
            return self.findPeakElementHelper(nums, middle+1, right)


s = Solution()

assert 2 == s.findPeakElement([1, 2, 3, 2, 5])
assert (1 == s.findPeakElement([1, 2, 1, 3, 5, 6, 4]) or (5 == s.findPeakElement([1, 2, 1, 3, 5, 6, 4])))
assert 3 == s.findPeakElement([1, 2, 3, 4])
assert 1 == s.findPeakElement([1, 2])
assert 0 == s.findPeakElement([2, 1])
assert 0 == s.findPeakElement([5])
