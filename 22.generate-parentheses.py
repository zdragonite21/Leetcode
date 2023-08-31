#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#


# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(l, r, s):
            if len(s) == n * 2:
                res.append(s)
            if l < n:
                dfs(l + 1, r, s + "(")
            if r < l:
                dfs(l, r + 1, s + ")")

        dfs(0, 0, "")
        return res


# @lc code=end
