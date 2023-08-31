#
# @lc app=leetcode id=992 lang=python3
#
# [992] Subarrays with K Different Integers
#
from collections import Counter

# @lc code=start
# class Solution:
#     def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
#         dp = [[[] for __ in range(len(nums))] for _ in range(len(nums))]
#         ans = 0

#         for i in range(len(nums)):
#             dp[i][i].append(nums[i])
#             if k == 1:
#                 ans += 1

#         for l in range(2, len(nums) + 1):
#             for i in range(len(nums) - l + 1):
#                 j = i + l - 1
#                 n = len(dp[i][j - 1])
#                 if nums[j] in dp[i][j - 1]:
#                     dp[i][j] = dp[i][j - 1]
#                     if n == k:
#                         ans += 1
#                 else:
#                     dp[i][j] = dp[i][j - 1]
#                     dp[i][j].append(nums[j])
#                     if n + 1 == k:
#                         ans += 1


#         return ans
# class Solution:
#     def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
#         # dp = [[0]*len(nums) for _ in range(len(nums))]
#         ans = 0
#         c = Counter()

#         # for i in range(len(nums)):
#         #     dp[i][i] = 1
#         #     if k == 1:
#         #         ans += 1
#         if k == 1:
#             ans += len(nums)

#         for i in range(len(nums) - 1):
#             c = Counter()
#             c[nums[i]] += 1
#             u = 1
#             for l in range(2, len(nums) - i + 1):
#                 # print(u, c)
#                 j = i + l - 1
#                 if c[nums[j]] == 0:
#                     u += 1
#                 c[nums[j]] += 1
#                 if u == k:
#                     ans += 1
#         return ans

#         # for l in range(2, len(nums) + 1):
#         #     for i in range(len(nums) - l + 1):
#         #         j = i + l - 1
#         #         n = len(dp[i][j - 1])
#         #         if nums[j] in dp[i][j - 1]:
#         #             dp[i][j] = dp[i][j - 1]
#         #             if n == k:
#         #                 ans += 1
#         #         else:
#         #             dp[i][j] = dp[i][j - 1]
#         #             dp[i][j].append(nums[j])
#         #             if n + 1 == k:
#         #                 ans += 1


#         # return ans
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMost(kval):
            c = Counter()
            ans = 0
            i = 0
            kv = 0
            for j in range(len(nums)):
                if c[nums[j]] == 0:
                    kv += 1
                c[nums[j]] += 1
                while kv > kval:
                    c[nums[i]] -= 1
                    if c[nums[i]] == 0:
                        kv -= 1
                    i += 1
                ans += j - i + 1  # understand this line
            return ans

        # print(atMost(k))
        return atMost(k) - atMost(k - 1)


# @lc code=end
