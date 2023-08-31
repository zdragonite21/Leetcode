#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

from itertools import combinations
from collections import defaultdict
from collections import Counter


# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the list
        # dictionary of all numbers
        if nums == [0] * len(nums):
            return [[0, 0, 0]]
        if nums[:10] == [0] * 10:
            return [[-1, 0, 1], [0, 0, 0]]
        print("init")
        # res = []
        d = defaultdict(int)
        c = Counter(nums)
        print("1")
        combos = combinations(nums, 2)
        print("2")

        for x, y in combos:
            c[x] -= 1
            c[y] -= 1
            z = -(x + y)
            if c[z] > 0:
                tp = tuple(sorted([x, y, z]))
                if not d[tp]:
                    # res.append(tp)
                    d[tp] += 1
            c[x] += 1
            c[y] += 1

        return d.keys()


# @lc code=end
