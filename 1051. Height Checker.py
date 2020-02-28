# Students are asked to stand in non-decreasing order of heights for an annual photo.
#
# Return the minimum number of students that must move in order for all students to
# be standing in non-decreasing order of height.
#
# Example 1:
#
# Input: heights = [1,1,4,2,1,3]
# Output: 3
#
# Constraints:
#
# 1 <= heights.length <= 100
# 1 <= heights[i] <= 100

from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ct = 0
        sorted_heights = sorted(heights)
        for i in range(len(heights)):
            if sorted_heights[i] != heights[i]:
                ct += 1
        return ct


s = Solution()

assert 3 == s.heightChecker([1,1,4,2,1,3])
