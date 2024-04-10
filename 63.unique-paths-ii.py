#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#


## first solution
# if obstacleGrid[0][0]:
#             return 0
#         dp = [[x * -1 for x in row] for row in obstacleGrid]
#         print(dp)
#         for i in range(len(dp)):
#             for j in range(len(dp[0])):
#                 if not i and not j:
#                     dp[0][0] = 1
#                 elif not dp[i][j] == -1:
#                     left = 0 if j <= 0 or dp[i][j - 1] == -1 else dp[i][j - 1]
#                     top = 0 if i <= 0 or dp[i - 1][j] == -1 else dp[i - 1][j]
#                     dp[i][j] = left + top
#         print(dp)
#         return dp[-1][-1] if not dp[-1][-1] == -1 else 0
# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0][1] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if not obstacleGrid[i - 1][j - 1]:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]

    # @lc code=end
