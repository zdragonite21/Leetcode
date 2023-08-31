#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#


# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        d = [[] for _ in range(numRows)]
        x = 0
        diag = False
        for i in range(len(s)):
            # print(x)
            d[x].append(s[i])
            if x == 0:
                diag = False
            if x == numRows - 1 or diag:
                x -= 1
                diag = True
            else:
                x += 1

        ss = ""
        for y in d:
            ss += "".join(y)

        return ss


# @lc code=end
