#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#


# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        sign = 1
        start = 0
        if s[0] == "-":
            sign = -1
            start = 1
        elif s[0] == "+":
            start = 1
        n = ""
        for x in s[start:]:
            if x.isdigit():
                n += x
            else:
                break
        if not n:
            return 0
        # print(n, s)
        # print(2**31 - 1)
        # print(-(2**31))
        n = int(n)
        if sign == 1:
            n = 2**31 - 1 if n > 2**31 - 1 else n
        else:
            n = -(2**31) if n * sign < -(2**31) else n * sign
        return n


# @lc code=end
