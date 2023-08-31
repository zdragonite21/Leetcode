#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#


# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def dfs(m):
            if len(m) == 0:
                return 0
            if len(m) == 1:
                return 1
            if len(m) == 2:
                return max(max(m), sum(m))

            ms = len(m) // 2
            a = dfs(m[:ms])
            b = dfs(m[ms:])
            c = max(a, b)
            return max(a + b, c)


# @lc code=end
