#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#
from itertools import permutations


# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1

        if i == 0:
            nums.reverse()
            return

        p = i - 1
        f = len(nums) - 1
        while nums[f] <= nums[p]:
            f -= 1

        nums[f], nums[p] = nums[p], nums[f]

        j = len(nums) - 1
        while j > i:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1


# @lc code=end
