#56. Merge Intervals
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
from typing import List
from operator import itemgetter

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0 or len(intervals) == 1:
            return intervals
        intervals = sorted(intervals, key=itemgetter(0))
        i = 1
        return_list = []
        curr_interval = intervals[0]
        while (i < len(intervals)):
            if curr_interval[1] >= intervals[i][0]:
                curr_interval = [curr_interval[0], max(curr_interval[1], intervals[i][1])]
            else:
                return_list.append(curr_interval)
                curr_interval = intervals[i]
            i += 1
        return_list.append(curr_interval)
        return return_list

s = Solution()
assert [[]] == s.merge([[]])
assert [[1,5]] == s.merge([[1,5]])
assert [[1,4]] == s.merge([[1,4],[2,3]])
assert [[1,4]] == s.merge([[1,2], [2,3], [3,4]])
print("**********************************************")
assert [[1,6],[8,10],[15,18]] == s.merge([[1,3],[2,6],[8,10],[15,18]])
print("**********************************************")
assert [[1,6],[8,10],[15,18]] == s.merge([[1,3],[15,18],[2,6],[8,10]])
print("**********************************************")
assert [[1,5]] == s.merge([[1,4],[4,5]])
