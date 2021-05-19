# Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.
from typing import List
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        first = 0
        last = len(A) - 1

        squares_list = []
        while first <= last:
            if abs(A[first]) > abs(A[last]):
                squares_list.insert(0, A[first] ** 2)
                first += 1
            else:
                squares_list.insert(0, A[last] ** 2)
                last -= 1

        return squares_list


    def sortedSquares2(self, A: List[int]) -> List[int]:
        print(sorted([x ** 2 for x in A]))
        return sorted([x ** 2 for x in A])


s = Solution()
assert [0,1,9,16,100] == s.sortedSquares([-4,-1,0,3,10])
assert [4,9,9,49,121] == s.sortedSquares([-7,-3,2,3,11])


assert [0,1,9,16,100] == s.sortedSquares2([-4,-1,0,3,10])
assert [4,9,9,49,121] == s.sortedSquares2([-7,-3,2,3,11])
