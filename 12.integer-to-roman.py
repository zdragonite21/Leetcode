#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#


# @lc code=start


class Solution:
    def intToRoman(self, num: int) -> str:
        d = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M",
        }

        k = list(d.keys())

        def bf(n):
            l = -1
            r = len(k)
            while r - l > 1:
                m = (l + r) // 2
                if n < k[m]:
                    r = m
                else:
                    l = m
            # print(n, l)
            return k[l]

        s = ""
        while num > 0:
            x = bf(num)
            num -= x
            s += d[x]
            # print(x, num)

        return s


# @lc code=end
