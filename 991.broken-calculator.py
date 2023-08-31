#
# @lc app=leetcode id=991 lang=python3
#
# [991] Broken Calculator
#


# @lc code=start
class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        if startValue > target:
            return startValue - target

        total = 0
        two = 0
        ones = 0
        x = startValue
        while x < target:
            x *= 2
            two += 1
        while x != target:
            x -= 1
            ones += 1
        total += two
        y = 2**two
        while ones > 1:
            while y > ones and two > 0:
                two -= 1
                y = 2**two
            total += ones // (2**two)
            ones = ones % (2**two)
        total += ones % (2**two)
        return int(total)


# @lc code=end
