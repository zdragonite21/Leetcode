#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#


# @lc code=start
class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        sweep = []
        ans = []
        for l, r in intervals:
            sweep.append((l, 0))
            sweep.append((r, 1))
        sweep.append((newInterval[0], 0))
        sweep.append((newInterval[1], 1))
        sweep.sort()

        print(sweep)

        l, r = -1, -1
        for i, (x, y) in enumerate(sweep):
            if y:
                if i + 1 >= len(sweep) or not sweep[i + 1][1]:
                    r = x
                    ans.append((l, r))
                    l, r = -1, -1
            else:
                if l == -1:
                    l = x

        return ans
        # @lc code=end
