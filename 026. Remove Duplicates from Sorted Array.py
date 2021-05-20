# Given a sorted array nums, remove the duplicates in-place such that each element appears
# only once and returns the new length.
#
# Do not allocate extra space for another array, you must do this by modifying the
# input array in-place with O(1) extra memory.
#
# Clarification:
#
# Confused why the returned value is an integer but your answer is an array?
#
# Note that the input array is passed in by reference, which means a modification to the input
# array will be known to the caller as well.
#
# Internally you can think of this:
#
# // nums is passed in by reference. (i.e., without making a copy)
# int len = removeDuplicates(nums);
#
# // any modification to nums in your function would be known by the caller.
# // using the length returned by your function, it prints the first len elements.
# for (int i = 0; i < len; i++) {
#     print(nums[i]);
# }




from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # since remove is slow, instead just keep a second index which is the
        # index of the "new" array.  While iterating through the array normally,
        # any time a "new" element is found, add it to the current index of the
        # "new" array then slice the array to that index at the end

        if len(nums) == 0:
            return 0
        i = 0
        for ct in range(1, len(nums)):
            if nums[i] != nums[ct]:
                i += 1
                nums[i] = nums[ct]

        nums = nums[0:i+1]
        return len(nums), nums

        # remove is slow...
        # if len(nums) == 0:
        #     return 0
        # curr = nums[0]
        # ct = 1
        # while ct < len(nums):
        #     if curr == nums[ct]:
        #         nums.remove(nums[ct])
        #     else:
        #         curr = nums[ct]
        #         ct += 1
        # return len(nums)

s = Solution()


assert (2, [1,2]) == s.removeDuplicates([1,1,2])
assert (5, [0,1,2,3,4]) == s.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
