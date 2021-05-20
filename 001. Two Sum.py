# Given an array of integers nums and an integer target, return indices of the two numbers such that they
# add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.


from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Put into a dictionary the value of target - item as the key and index as the value
        # Subsequently if the key exists, return its index and the current index
        d = {}
        for i in range(0, len(nums)):
            diff = target - nums[i]
            if nums[i] in d:
                return [d[nums[i]], i]
            else:
                d[diff] = i
        return


        #     diff = abs(target - nums[i])
        #     print("diff: " + str(diff))
        #     if (nums[i] in d):
        #         print([d[diff], i])
        #         return [d[diff], i]
        #     else:
        #         print(f"adding {i} at {diff}")
        #         d[diff] = i
        #     print(d)
        # print("Finished")


s = Solution()
assert [0,1] == s.twoSum([2,7,11,15], 9)
assert [1,2] == s.twoSum([3,2,4], 6)
assert [0,1] == s.twoSum([3,3], 6)
assert [2,4] == s.twoSum([-1,-2,-3,-4,-5], -8)
