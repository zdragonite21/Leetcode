#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#


# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()

        def dfs(n, back=[]):
            # print(n)
            if n == 0:
                ans.add(tuple(sorted(back)))
                return
            for x in candidates:
                if n - x >= 0:
                    dfs(n - x, back + [x])

        dfs(target, [])
        return ans


# @lc code=end
