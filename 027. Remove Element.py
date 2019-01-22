#27. Remove Element

# Given an array nums and a value val, remove all instances of that value in-place and return the new length.
#
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
#
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        prev = 0
        for ct in range(len(nums)):
            if nums[ct] != val:
                nums[prev] = nums[ct]
                prev += 1
        return prev





s = Solution()

assert s.removeElement([], 0) == 0
assert s.removeElement([1,2,3], 4) == 3
assert s.removeElement([3,2,2,3], 3) == 2
assert s.removeElement([0,1,2,2,3,0,4,2], 2) == 5
assert s.removeElement([1,1,1], 1) == 0
assert s.removeElement([1,1,2], 1) == 1
assert s.removeElement([1,2,1], 1) == 1
