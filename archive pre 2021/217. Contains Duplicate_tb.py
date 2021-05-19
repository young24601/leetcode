from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = set()
        for item in nums:
            if item in d:
                return True
            else:
                d.add(item)
        return False



    def containsDuplicate2(self, nums: List[int]) -> bool:
        xor_temp = nums[0]
        for item in nums[1:]:
            print(xor_temp, "^", item, "=", xor_temp ^ item)
            xor_temp = xor_temp ^ item

        print("final value is", xor_temp)
        return True




s = Solution()
assert True == s.containsDuplicate([1,2,3,1])
assert True == s.containsDuplicate([1,1,1,3,3,4,3,2,4,2])
assert False == s.containsDuplicate([1,2,3,4])
