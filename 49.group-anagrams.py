#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#


# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ss = [("".join(sorted(strs[i])), i) for i in range(len(strs))]
        ss.sort()
        res = []
        for i in range(len(ss)):
            if i > 0 and ss[i][0] == ss[i - 1][0]:
                res[-1].append(strs[ss[i][1]])
                continue
            res.append([strs[ss[i][1]]])
        return res


# @lc code=end
