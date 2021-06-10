# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.


from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # should be able to use greedy algo to do the count
        current_sum = 0
        max_sum = nums[0]
        for item in nums:
            if max_sum < 0 and item > max_sum:
                current_sum = item
                max_sum = item
            else:
                current_sum += item
            if current_sum < 0:
                current_sum = 0
            elif current_sum > max_sum:
                max_sum = current_sum
        return max_sum


s = Solution()
assert 6 == s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
assert 1 == s.maxSubArray([1])
assert 23 == s.maxSubArray([5,4,-1,7,8])
assert -1 == s.maxSubArray([-1])
assert 5 == s.maxSubArray([5,-1,-2,-1,3,-1])
assert -2 == s.maxSubArray([-4,-3,-2,-2,-4])
assert -1 == s.maxSubArray([-2,-1])
