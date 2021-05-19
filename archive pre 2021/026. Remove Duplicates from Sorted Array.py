#26. Remove Duplicates from Sorted Array

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return 0

        index = 0

        for ct in range(1, len(nums)):
            if nums[ct] != nums[index]:
                index += 1
                nums[index] = nums[ct]
        index += 1
        nums = nums[0:index]
        print(nums)

        return index


s = Solution()
assert s.removeDuplicates([1,1,2]) == 2
assert s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]) == 5
assert s.removeDuplicates([]) == 0
assert s.removeDuplicates([1,1,1,1,1,1,1,1,1,1,1]) == 1
