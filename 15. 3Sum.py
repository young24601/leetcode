#15. 3Sum

# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
# Find all unique triplets in the array which gives the sum of zero.
# 
# Note:
# 
# The solution set must not contain duplicate triplets.
# 
# Example:
# 
# Given array nums = [-1, 0, 1, 2, -1, -4],
# 
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # a reasonable solution would be to fix on each array index and use the solution for two sum (which was O(n))
        # twoSum needs to be modified to return multiple solutions and also to return the values (instead of indices)
        result = []
        nums.sort()
        prev = None
        for ct in range(0,len(nums)):
            print("checking",prev,"vs",nums[ct])
            if prev == nums[ct]:
                continue
            prev = nums[ct]
            res = self.twoSum(nums[ct+1:], -nums[ct])            
            if res != [] and res != False:
                for item in res:
                    result.append(item)
        return result


    def twoSum(self, nums, target):
        print("Testing", nums, "with", target)
        if len(nums) <= 1:
            return False
        comp = {}
        res = []
        for x in range(len(nums)):
            if (nums[x]) in comp:
                print("found", [nums[comp[nums[x]]], nums[x], -target])
                if [nums[comp[nums[x]]], nums[x], -target] not in res:
                    res.append([nums[comp[nums[x]]], nums[x], -target])
                    print("res:",res)

            else:
                comp[(target - nums[x])] = x
        return res


s = Solution()
#print(s.threeSum([-1, 0, 1, 2, -1, -4]))
print(s.threeSum([0,0,0,0]))
