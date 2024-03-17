#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#


# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = curMax = nums[0]
        for num in nums[1:]:
            curMax = max(curMax + num, num)
            maxSum = max(maxSum, curMax)

        return maxSum


# @lc code=end
