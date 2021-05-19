from typing import List


#solve without division in O(n)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        sums = [1]
        for item in nums[:-1]:
            product *= item
            sums.append(product)
        product = 1
        for i in range(len(nums)-1, -1, -1):
            sums[i] *= product
            product *= nums[i]
        return sums



s = Solution()
assert [24, 12, 8, 6] == s.productExceptSelf([1,2,3,4])
