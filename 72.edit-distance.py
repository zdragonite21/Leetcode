#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# n1 = len(word1)
#         n2 = len(word2)
#         dp = [[float("inf")] * (n2 + 1) for _ in range(n1 + 1)]
#         for i in range(n1 + 1):
#             dp[i][-1] = n1 - i
#         for j in range(n2 + 1):
#             dp[-1][j] = n2 - j

#         for i in range(n1 - 1, -1, -1):
#             for j in range(n2 - 1, -1, -1):
#                 if word1[i] == word2[j]:
#                     dp[i][j] = dp[i + 1][j + 1]
#                 else:
#                     dp[i][j] = 1 + min([dp[i][j + 1], dp[i + 1][j], dp[i + 1][j + 1]])
#         for d in dp:
#             print(d)
#         return dp[0][0]


# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        prev = [i for i in range(n + 1)]
        cur = [0] * (n + 1)

        for i in range(1, m + 1):
            cur[0] = i
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    cur[j] = prev[j - 1]
                else:
                    cur[j] = 1 + min(prev[j], cur[j - 1], prev[j - 1])

            prev = cur
            cur = [0] * (n + 1)

        return prev[-1]


# @lc code=end
