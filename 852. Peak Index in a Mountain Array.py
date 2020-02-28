# Let's call an array A a mountain if the following properties hold:
#
# A.length >= 3
# There exists some 0 < i < A.length - 1 such that
# A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
# Given an array that is definitely a mountain, return any i such that
# A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

from typing import List
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:

        first = 0
        last = len(A) - 1
        mid = (first + last) // 2

        while 1:
            if A[mid-1] < A[mid]:
                if A[mid] > A[mid+1]: # A[mid-1] < A[mid] < A[mid+1] found max
                    return mid
                else: # A[mid-1] < A[mid] and A[mid] < a[mid+1] so move right
                    first = mid
            else: # since A[mid] > A[mid-1] and it is a mountain, move left
                last = mid
            mid = (first + last) // 2

        return -1


s = Solution()
assert 1 == s.peakIndexInMountainArray([0,1,0])
assert 1 == s.peakIndexInMountainArray([0,2,1,0])
