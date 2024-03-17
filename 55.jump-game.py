#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#


# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        mn = n - 1
        for i in range(n - 2, -1, -1):
            if nums[i] + i >= mn:
                mn = i
        return mn == 0


# @lc code=end
