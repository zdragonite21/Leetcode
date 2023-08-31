from itertools import combinations

#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#


# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 3:
            return sum(nums)

        nums.sort()
        n = nums

        res = 0
        d = 10e10
        for i in range(len(n) - 2):
            l = i + 1
            r = len(n) - 1
            while l < r:
                s = n[i] + n[l] + n[r]
                diff = s - target
                if diff == 0:
                    return s

                if abs(diff) < d:
                    res = s
                    d = abs(diff)

                if diff > 0:
                    r -= 1
                if diff < 0:
                    l += 1
        return res

        # ne = []
        # pe = []
        # zeros = []
        # for x in sorted(nums):
        #     if x > 0:
        #         pe.append(x)
        #     elif x < 0:
        #         ne.append(x)
        #     else:
        #         zeros.append(x)

        # # 0 0 0
        # if target == 0 and len(zeros) >= 3:
        #     return 0

        # # + 0 0, - 0 0
        # if len(zeros) >= 2:
        #     ls = pe if target > 0 else ne
        #     if not pe:
        #         ls = ne
        #     if not ne:
        #         ls = pe
        #     if target > 0:
        #         diff = 10e10
        #         res = 0
        #         for x in ls:
        #             if abs(x - target) < diff:
        #                 diff = abs(x - target)
        #                 res = x
        #         return x
        # # + + 0, - - 0, + - 0
        # if len(zeros) >= 1:

        # res = 0
        # d = 10e10
        # for x, y, z in combinations(nums, 3):
        #     s = sum([x, y, z])
        #     diff = abs(target - s)
        #     if diff < d:
        #         d = diff
        #         res = s

        # return res


# @lc code=end
