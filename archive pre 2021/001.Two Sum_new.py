from typing import List
'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twoSumDictionary = {}
        for i in range(len(nums)):
            if nums[i] in twoSumDictionary:
                return[twoSumDictionary[nums[i]], i]
            else:
                twoSumDictionary[target-nums[i]] = i


s = Solution()
assert [1,3] == s.twoSum([2,7,11,15], 22)
assert [1,2] == s.twoSum([3,2,4], 6)
assert [0,1] == s.twoSum([3,3], 6)
