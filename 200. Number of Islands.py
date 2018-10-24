# 200. Number of Islands


class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # when you find an "island" (1), you mark all adjacent 1s so that you don't
        # count them again.
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':

                    self.dfs(grid, i, j)
                    count += 1
        print("ct:", count)
        return count

    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return
        print("i,j:", i,j, "| len(grid): ", len(grid), "| len(grid[0]): ", len(grid[0]), "| grid[i][j]: ", grid[i][j])

        grid[i][j] = 'X'
        for item in grid:
            print(item)
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)




s = Solution()
assert 2 == s.numIslands([["1","1","1","1","1","1"],["1","0","0","0","0","1"],["1","0","1","1","0","1"],["1","0","0","0","0","1"],["1","1","1","1","1","1"]])
#assert 1 == s.numIslands([['1', '1', '1', '1', '0'], ['1', '1', '0', '1', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '0', '0', '0']])
#assert 3 == s.numIslands([['1', '1', '0', '0', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '1', '0', '0'], ['0', '0', '0', '1', '1']])
