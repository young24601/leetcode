# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
#
# Your algorithm should run in O(n) complexity.
#
# Example:
#
# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums) # place nums into a set to remove duplicates
        longest = 0
        while nums_set != set():
            elements_left = 0
            elements_right = 0
            p = nums_set.pop() #grab a number

            x = p+1 # check for numbers to the right
            while x in nums_set:
                nums_set.remove(x)
                x = x+1
                elements_right += 1
            x = p-1 # numbers to the left
            while x in nums_set:
                nums_set.remove(x)
                x = x-1
                elements_left += 1

            longest = max(longest, elements_left+elements_right+1)
        return longest



s = Solution()
assert 0 == s.longestConsecutive([])
assert 1 == s.longestConsecutive([213312312])
assert 3 == s.longestConsecutive([1,2,0,1])
assert 4 == s.longestConsecutive([100, 4, 200, 1, 3, 2])
assert 7 == s.longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6])



    # def longestConsecutive(self, nums: List[int]) -> int:
    #     if len(nums) <= 1:
    #         return len(nums)
    #
    #     sorted_list = [nums[0]]
    #
    #     for ct in range(1, len(nums)):
    #         if nums[ct] not in sorted_list:
    #             b = bisect.bisect(sorted_list, nums[ct])
    #             sorted_list = sorted_list[:b] + [nums[ct]] + sorted_list[b:]
    #     max = 1
    #     current_count = 1
    #     curr = sorted_list[0]
    #     print(sorted_list, curr)
    #
    #     for ct in range(1, len(sorted_list)):
    #         print(sorted_list[ct], "vs", curr)
    #         if sorted_list[ct] == curr+1:
    #             current_count += 1
    #             print("match")
    #         else:
    #             if current_count > max:
    #                 max = current_count
    #             current_count = 1
    #             print("no")
    #         print("setting curr to", sorted_list[ct])
    #         curr = sorted_list[ct]
    #
    #     if current_count > max:
    #         max = current_count
    #
    #     return max
