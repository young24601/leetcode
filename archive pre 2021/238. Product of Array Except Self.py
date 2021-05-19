# 
# Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
# 
# Solve it without division and in O(n).
# 
# For example, given [1,2,3,4], return [24,12,8,6].
# 
# Follow up:
# Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)


class Solution:
    def productExceptSelf(self, nums):
        if len(nums) == 1:
            return [0]
        
        output = []
        x = 1
        for ct in range(0, len(nums)):
            output.append(x)
            x = x * nums[ct]

        x = 1
        for ct in range(len(nums)-1, -1, -1):
            output[ct] *= x
            x = x * nums[ct]        
        
        return output
        
        
        
        
test = Solution()
#print(test.productExceptSelf([1])) #0
print(test.productExceptSelf([1,2,3,4])) #[24,12,8,6]