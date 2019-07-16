from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        comp_dict = {}

        for i in range(len(nums)):
            print("Testing", nums[i], "in", comp_dict)
            if nums[i] in comp_dict:
                print("Found", i, comp_dict[nums[i]])
                return [comp_dict[nums[i]], i]
            else:
                print("Index", target-nums[i], "stores", i)
                comp_dict[target-nums[i]] = i
        print(comp_dict)


s = Solution()
assert [0,1] == s.twoSum([2, 7, 11, 15], 9)
