#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#


# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # dp or sliding window
        h = height
        i = 0
        j = len(h) - 1
        mx = 0
        while j > i:
            mx = max(mx, min(h[i], h[j]) * (j - i))
            if h[i] > h[j]:
                j -= 1
            else:
                i += 1
        return mx


# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         # dp or sliding window
#         h = height
#         # dp = [[0] * len(h) for _ in range(len(h))]  # max water i, j
#         mx = 0
#         for l in range(2, len(h) + 1):
#             for i in range(len(h) - l + 1):
#                 j = i + l - 1
#                 mx = max(mx, min(h[i], h[j]) * (l - 1))

#                 # dp[i][j] = max([dp[i + 1][j], dp[i][j - 1], min(h[i], h[j]) * (l - 1)])
#                 # print(dp[i][j], i, j)
#         return mx


# @lc code=end
