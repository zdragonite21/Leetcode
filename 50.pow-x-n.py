#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#


# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # return x**n

        # y = x
        # if n == 0:
        #     return 1
        # if n == 1:
        #     return x
        # if n == -1:
        #     return 1 / x
        # if n < 0:
        #     y = 1 / x

        # if n % 2 == 0:
        #     return self.myPow(x, n // 2) * self.myPow(x, n // 2)
        # else:
        #     return y * self.myPow(x, n // 2) * self.myPow(x, n // 2)

        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        elif n > 0:
            m = n // 2
            if n % 2 == 0:
                return self.myPow(x * x, m)
            else:
                return x * self.myPow(x * x, m)


# @lc code=end
