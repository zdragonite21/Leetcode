#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#


# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        x = 0
        a = 1
        for n1 in num1[::-1]:
            b = 1
            for n2 in num2[::-1]:
                x += int(n1) * int(n2) * a * b
                b *= 10
            a *= 10
        return str(x)


# @lc code=end
