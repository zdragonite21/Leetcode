#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#


# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []

        intervals.sort()

        cur = intervals[0]
        for interval in intervals[1:]:
            l1, r1 = cur
            l2, r2 = interval
            if r1 >= l2:
                cur = [min(l1, l2), max(r1, r2)]
            else:
                ans.append(cur)
                cur = interval

        return ans + [cur]


# @lc code=end
