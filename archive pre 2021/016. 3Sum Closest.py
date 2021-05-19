#16. 3Sum Closest
# Given array nums = [-1, 2, 1, -4], and target = 1.
#
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# Given an array nums of n integers and an integer target, find three integers
# in nums such that the sum is closest to target. Return the sum of the three integers.
# You may assume that each input would have exactly one solution.


class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # need a new strategy.  not sure of a way to modify twoSum to efficiently return the closest value.
        # one possible solution is to sort the array.  We then fix the first element and then point to the second
        # and last elements.  When we do the sum, if the value is the target then return.  Otherwise, if the sum is smaller
        # than the target, then we need to increase the sum by incrementing to the third element.  If the sum is larger than
        # the target, then we need to move the rightmost pointer (to the third item) to the left to decrease the sum closer
        # to the target.  Once second and third meet, then we fix on the next value for first and reset second to first+1 and
        # third to the last index.

        nums.sort()
        best = nums[0] + nums[1] + nums[-1]
        if len(nums) == 3:
            return best

        for first in range(0, len(nums)):
            second = first + 1
            third = len(nums) - 1
            while (second < third):
                s = nums[first] + nums[second] + nums[third]
                if s == target:
                    return s
                if abs(target - s) < abs(target - best):
                    best = s
                if s > target:
                    third -= 1
                else:
                    second += 1
        return best


s = Solution()
# print(s.threeSumClosest([-1,2,1,-4], 1))
# print(s.threeSumClosest([0,0,0], 1))
# print(s.threeSumClosest([1,1,1,1], 3))
# print(s.threeSumClosest([1,1,-1,-1,3], -1))
print(s.threeSumClosest([-1,0,1,1,55], 3))
