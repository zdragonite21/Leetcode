#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#


# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not i and not j:
                    continue
                if not i:
                    grid[i][j] += grid[i][j - 1]
                elif not j:
                    grid[i][j] += grid[i - 1][j]
                else:
                    left = grid[i][j - 1]
                    top = grid[i - 1][j]
                    grid[i][j] += min(left, top)

        return grid[-1][-1]


# @lc code=end
