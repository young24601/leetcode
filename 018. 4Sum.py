#18. 4Sum
# Given an array nums of n integers and an integer target, are there elements a, b, c, and d in
# nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
#
# Note:
#
# The solution set must not contain duplicate quadruplets.

class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # use previous threeSum implementation to do fourSum
        nums.sort()
        print("nums:", nums)
        sol = []
        for ct in range(0, len(nums)):
            print("fixing on", nums[ct], "running 3 sum on", nums[ct+1:], "with target", target-nums[ct])
            res4 = self.threeSum(nums[ct+1:], target-nums[ct])
            if res4 != []:
                for item in res4:
                    print("4sum:", [nums[ct]] + item)
                    if [nums[ct]] + item not in sol:
                        sol.append([nums[ct]] + item)
                    print(sol)
        return sol

    def threeSum(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # a reasonable solution would be to fix on each array index and use the solution for two sum (which was O(n))
        # twoSum needs to be modified to return multiple solutions and also to return the values (instead of indices)
        result = []
        nums.sort()
        print("nums:",nums)
        prev = None
        for ct in range(0,len(nums)):
            #print("checking",prev,"vs",nums[ct])
            if prev == nums[ct]:
                continue
            prev = nums[ct]
            #res = self.twoSum(nums[ct+1:], -nums[ct])
            #modify to use target
            print("Have ", nums[ct], "in", nums[ct+1:], "Going for ", target-nums[ct])
            res = self.twoSum(nums[ct+1:], target-nums[ct])
            if res != [] and res != False:
                for item in res:
                    print("**appended", [nums[ct]] + item)
                    #if [nums[ct]] + item not in result:
                    result.append([nums[ct]] + item)
        return result


    def twoSum(self, nums, target):
        print("Testing", nums, "with", target)
        if len(nums) <= 1:
            return False
        comp = {}
        res = []
        for x in range(len(nums)):
            if (nums[x]) in comp:
                print("found", [nums[comp[nums[x]]], nums[x]])
                if [nums[comp[nums[x]]], nums[x], target] not in res:
                    #res.append([nums[comp[nums[x]]], nums[x], target])
                    res.append([nums[comp[nums[x]]], nums[x]])
                    #print("res:",res)

            else:
                comp[(target - nums[x])] = x
        return res


s = Solution()
#print(s.fourSum([1, 0, -1, 0, -2, 2], 0))
#print(s.fourSum([5,5,3,5,1,-5,1,-2], 4))
print(s.fourSum([-1,-5,-5,-3,2,5,0,4], -7))

#print(s.threeSum([-1, 0, 1, 2, -1, -4], 0))

#print(s.twoSum([2, 7, 11, 15], 9))
