#
# @lc app=leetcode id=990 lang=python3
#
# [990] Satisfiability of Equality Equations
#
from collections import defaultdict


# @lc code=start
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        ee = defaultdict(set)
        ne = []
        for a, b, c, d in equations:
            if b == "=":
                if a == d:
                    continue
                ee[a].add(d)
                ee[d].add(a)
            if b == "!":
                if a == d:
                    return False
                ne.append((a, d))

        def dfs(s, t, v=set()):
            if s in v:
                return False
            if s == t:
                return True
            v.add(s)
            return any(dfs(x, t, v) for x in ee[s])

        return all(
            not dfs(x, y, set()) for x, y in ne if x in ee.keys() and y in ee.keys()
        )


# @lc code=end
