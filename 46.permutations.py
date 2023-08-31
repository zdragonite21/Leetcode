#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#


# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(ls):
            if len(ls) == 1:
                return [ls]
            if len(ls) == 2:
                return [ls, ls[::-1]]
            x = []
            for i in range(len(ls)):
                for z in dfs(ls[:i] + ls[i + 1 :]):
                    # print(ls[i], z)
                    x.append([ls[i]] + z)
            return x

        return dfs(nums)


# @lc code=end
