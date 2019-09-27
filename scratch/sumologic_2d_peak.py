#!/usr/bin/python3
from typing import List


class Solution:
    # first fix on the middle column and find the maximum of it.
    # if it is a peak then done.
    # else fix on the side with the bigger value and repeat
    # this is safe because like with the 1d version, you are always climbing up
    # and will eventually result in a peak.  also note that you don't have to check
    # previously visited columns once you go to a neighboring column because it is guaranteed
    # that you will not have a value greater than the new greatest value of the column (since
    # you went to the neighboring column using the column's max value.
    # easier to use numpy but done without it
    def findPeakElement2D(self, nums: List[int]) -> int:
        middle_column = (len(nums[0]) - 1) // 2
        max_index, max_value = max(enumerate([row[middle_column] for row in nums]), key=lambda p: p[1])

        # print(nums, middle_column, "len(nums)", len(nums))
        # print("max index", max_index, "max value", max_value)
        # print("max", nums[max_index][middle_column])

        # if left/right are smaller, then this is a peak
        if (middle_column == 0 or nums[max_index][middle_column] > nums[max_index][middle_column-1]) and (middle_column+1 == len(nums[0]) or nums[max_index][middle_column] > nums[max_index][middle_column+1]):
            return nums[max_index][middle_column]
        elif nums[max_index][middle_column-1] > nums[max_index][middle_column+1]:  # LHS bigger
            return self.findPeakElement2D([nums[i][0:middle_column] for i in range(0, len(nums))])
        else:  # RHS bigger
            return self.findPeakElement2D([nums[i][middle_column+1:] for i in range(0, len(nums))])

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
assert 7 == s.findPeakElement2D([[1], [4], [7]])
assert 10 == s.findPeakElement2D([[1, 2, 3], [4, 10, 6], [7, 8, 9]])
assert 9 == s.findPeakElement2D([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
assert 9 == s.findPeakElement2D([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
assert 20 == s.findPeakElement2D([[10, 8, 10, 10], [14, 13, 12, 11], [21, 9, 11, 16], [15, 17, 19, 20]])

assert 21 == s.findPeakElement2D([[10, 8, 10, 10, 11, 23, 14], [14, 13, 12, 11, 9, 1, 4], [15, 9, 11, 21, 3, 4, 5], [16, 17, 19, 20, 5, 8, 9]])
