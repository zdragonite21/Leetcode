#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#
# -------------------------------- solution 1 -------------------------------- #
# left = []
# right = []

# prev = newInterval
# for l, r in intervals:
#     a, b = prev
#     if r < a:
#         left.append([l, r])
#     elif l > b:
#         right.append([l, r])
#     else:
#         prev = [min(l, a), max(r, b)]

# return left + [prev] + right
import heapq


# @lc code=start
class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        h = []
        ans = []

        for l, r in intervals + [newInterval]:
            heapq.heappush(h, [l, -1])
            heapq.heappush(h, [r, 1])

        close, start = 0, None
        while h:
            x, val = heapq.heappop(h)
            close += val
            if start is None:
                start = x
            if not close:
                ans.append((start, x))
                start = None

        return ans
        # @lc code=end
