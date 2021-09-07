# https://leetcode.com/problems/number-of-islands/

class Solution(object):
    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != "1":
            return
        else:
            grid[i][j] = "2"  # mark visited, change from '1' (land) to '2' (visited)
            self.dfs(grid, i - 1, j)
            self.dfs(grid, i + 1, j)
            self.dfs(grid, i, j + 1)
            self.dfs(grid, i, j - 1)

    def numIslands(self, grid):
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    islands += 1
                    self.dfs(grid, i, j)
                # if it is '0' or '2', do nothing
        return islands

def test():
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    s = Solution()
    ans = s.numIslands(grid)
    assert ans == 1
