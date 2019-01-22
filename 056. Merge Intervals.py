#56. Merge Intervals


# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return []

        intervals = sorted(intervals, key = lambda x: x[0])
        curr = [intervals[0]]

        for i in intervals[1:]:
            if i[0] < curr[1]:






s = Solution()

assert [[1,6], [8,10], [15,18]] == s.merge([[1,3],[15,18], [2,6],[8,10]])
