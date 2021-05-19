from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = max_sum = nums[0]
        max_start_index = 0
        max_end_index = 0
        potential_end_index = 0

        for i in range(1, len(nums)-1):
            print("Processing", nums[i], "comparing", current_sum+nums[i], "with", max_sum)
            if current_sum + nums[i] > max_sum:
                print(" replacing max_sum", max_sum, "with current_sum", current_sum + nums[i])
                max_sum = current_sum + nums[i]
                max_end_index += 1
                potential_end_index = max_end_index
            elif current_sum + nums[i] > 0:
                potential_end_index += 1
                current_sum += nums[i]
            else:
                print(" reset")
                current_sum = nums[i]
                max_start_index = i




        print(max_start_index, "to", max_end_index, " max =", max_sum)





s = Solution()
s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) # [4,-1,2,1] has the largest sum = 6.
#assert 7 == s.maxSubArray([-2,1,-3,4,-1,2,1,-3,4]) # [4,-1,2,1] has the largest sum = 6.
