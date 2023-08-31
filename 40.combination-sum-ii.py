#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#


# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        candidates.sort()

        def dfs(cands, n, ls=[]):
            if n == 0:
                res.add(tuple(ls))
                return
            elif n < 0:
                return
            for i in range(len(cands)):
                if i > 0 and cands[i] == cands[i - 1]:
                    continue
                dfs(cands[i + 1 :], n - cands[i], ls + [cands[i]])

        dfs(candidates, target, [])
        return res


# @lc code=end
