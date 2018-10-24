#832. Flipping an Image

class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        # use a list comprehension to xor each element of each reversed row in A

        return([[1 ^ i for i in row[::-1]] for row in A])

test = Solution()


assert ([[1,0,0]] == test.flipAndInvertImage([[1,1,0]]))
assert ([[1,0,0],[0,1,0],[1,1,1]] == test.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))
assert ([[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]] == test.flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))
