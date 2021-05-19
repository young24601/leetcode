# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
#
# Example 1:
#
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:
#
# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix == []:
            return []

        left_limit = 0
        right_limit = len(matrix[0]) - 1
        top_limit = 0
        bottom_limit = len(matrix) - 1
        return_list = []
        while (left_limit <= right_limit and top_limit <= bottom_limit):
            for col in range(left_limit, right_limit+1):
                return_list.append(matrix[top_limit][col])
            top_limit += 1
            for row in range(top_limit, bottom_limit+1):
                return_list.append(matrix[row][right_limit])
            right_limit -= 1
            if (top_limit <= bottom_limit):
                for col in range(right_limit, left_limit-1, -1):
                    return_list.append(matrix[bottom_limit][col])
                bottom_limit -= 1
            if (left_limit <= right_limit):
                for row in range(bottom_limit, top_limit-1, -1):
                    return_list.append(matrix[row][left_limit])
                left_limit += 1

        return return_list

s = Solution()

output = s.spiralOrder([
])
print(output) # []

output = s.spiralOrder([
 [ 1 ]
])
print(output) # [1]

output = s.spiralOrder([
 [ 1 ],
 [ 4 ],
 [ 7 ]
])
print(output) # [1,4,7]
output = s.spiralOrder([
 [ 1, 2, 3 ]
 ])
print(output) # [1,2,3]

output = s.spiralOrder([
 [ 1, 2, 3, 4 ],
 [ 5, 6, 7, 8 ],
 [ 9, 10, 11, 12 ]
])
print(output) # [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

output = s.spiralOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
])
print(output) #[1,2,3,6,9,8,7,4,5]

output = s.spiralOrder([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
])
print(output) #[1,2,3,4,8,12,11,10,9,5,6,7]
