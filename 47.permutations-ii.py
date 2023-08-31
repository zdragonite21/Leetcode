#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#


# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(ls):
            if len(ls) == 1:
                return [ls]
            if len(ls) == 2:
                return [ls, ls[::-1]] if ls[0] != ls[1] else [ls]
            res = []
            for i in range(len(ls)):
                if i > 0 and ls[i] == ls[i - 1]:
                    continue
                for x in dfs(ls[:i] + ls[i + 1 :]):
                    res.append([ls[i]] + x)
            return res

        return dfs(sorted(nums))


# @lc code=end
