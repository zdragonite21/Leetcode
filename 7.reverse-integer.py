#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#


# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        neg = 1
        if x < 0:
            x *= -1
            neg = -1

        ls = []
        while x:
            ls.append(x % 10)
            x //= 10
        ans = 0
        y = 1
        while ls:
            ans += y * ls.pop()
            y *= 10

        if ans > 2**31 - 1 or ans < -(2**31):
            return 0
        return neg * ans


# @lc code=end
