# Let's call an array A a mountain if the following properties hold:
#
# A.length >= 3
# There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
# Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].


class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        return 0


s = Solution()
assert 1 == s.peakIndexInMountainArray([0,1,0])
assert 1 == s.peakIndexInMountainArray([0,2,1,0])
