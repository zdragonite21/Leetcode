#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#


# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        # Time Exceed
        # def dfs(ls):
        #     if len(ls) == 0 or len(ls) == 1:
        #         return 0
        #     if ls[0] == 0:
        #         return 10e10
        #     if len(ls) == 2:
        #         return 1
        #     return 1 + min(dfs(ls[i:]) for i in range(ls[0], 0, -1) if i < len(nums))

        # return dfs(nums)

        # greedy
        n = 0
        j = len(nums) - 1
        while j > 0:
            i = j - 1
            nx = 0
            while i >= 0:
                if nums[i] >= j - i:
                    nx = i
                i -= 1
            j = nx
            n += 1
        return n


# @lc code=end
