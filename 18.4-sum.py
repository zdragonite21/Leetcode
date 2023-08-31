#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#
from itertools import combinations
from collections import Counter


# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # c = Counter(nums)
        # res = set()
        # for x, y, z in combinations(nums, 3):
        #     c[x] -= 1
        #     c[y] -= 1
        #     c[z] -= 1
        #     s = x + y + z
        #     if c[target - s] > 0:
        #         res.add(tuple(sorted((x, y, z, target - s))))
        #     c[x] += 1
        #     c[y] += 1
        #     c[z] += 1

        # return res

        # return {
        #     tuple(sorted(combo))
        #     for combo in combinations(nums, 4)
        #     if sum(combo) == target
        # }

        nums.sort()
        n = nums
        res = set()
        for i in range(len(n) - 3):
            for j in range(i + 1, len(n) - 2):
                l = j + 1
                r = len(n) - 1
                # print(i, j, l, r)
                while r > l:
                    s = (n[i], n[j], n[l], n[r])
                    ns = sum(s)
                    # break
                    if ns == target:
                        res.add(s)
                        l += 1
                        r -= 1
                        while l < r and n[l] == n[l - 1]:
                            l += 1
                        while l < r and n[r] == n[r + 1]:
                            r -= 1

                    elif ns > target:
                        r -= 1
                    else:
                        l += 1
        return res


# @lc code=end
