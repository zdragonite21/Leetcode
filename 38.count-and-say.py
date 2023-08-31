#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#


# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        if n == 2:
            return "11"

        s = self.countAndSay(n - 1)

        res = ""
        i = 0
        j = 1
        x = 1
        while j < len(s):
            while j < len(s) and s[i] == s[j]:
                j += 1
                x += 1
            res += str(x) + s[i]
            i = j
            j = i + 1
            x = 1
        if s[-1] != s[-2]:
            res += str(1) + s[-1]

        return res


# @lc code=end
