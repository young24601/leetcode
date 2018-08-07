class Solution(object):
    def twoSumN2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for x in range (0, len(nums)):
            for y in range (1, len(nums)):
                if x != y:
                    if nums[x] + nums[y] == target:
                        return [x,y]
        
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        comp = {}
        for x in range(len(nums)):
            if (nums[x]) in comp:
                return([comp[nums[x]], x])
            else:
                comp[(target - nums[x])] = x

    #this one returns the actual values and multiple solutions
    def twoSum2(self, nums, target):
        if len(nums) <= 1:
            return False
        comp = {}
        res = []
        for x in range(len(nums)):
            if (nums[x]) in comp:
                res.append([nums[comp[nums[x]]], nums[x], target])
            else:
                comp[(target - nums[x])] = x
        return(res)
###########################

test = Solution()
print(test.twoSum2([2,7,11,15], 9))
print(test.twoSum2([3,2,4,1,5],6))