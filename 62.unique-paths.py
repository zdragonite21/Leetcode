#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#


# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [0] * n
        cur = [1] * n

        for i in range(1, m):
            prev = cur
            for j in range(1, n):
                cur[j] = prev[j] + cur[j - 1]

        return cur[-1]


# @lc code=end
