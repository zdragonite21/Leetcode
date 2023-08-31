#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#


# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        neg = not ((dividend > 0) is (divisor > 0))
        dd, d = abs(dividend), abs(divisor)
        res = 0

        while dd >= d:
            tmp, i = d, 1
            while dd >= tmp:
                dd -= tmp
                res += i
                i <<= 1
                tmp <<= 1
        if neg:
            res = -res

        return min(max(-2147483648, res), 2147483647)


# @lc code=end
