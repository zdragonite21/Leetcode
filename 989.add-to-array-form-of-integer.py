#
# @lc app=leetcode id=989 lang=python3
#
# [989] Add to Array-Form of Integer
#


# @lc code=start
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = sum(10**i * num[-(i + 1)] for i in range(len(num))) + k

        ls = []
        while n:
            ls.insert(0, n % 10)
            n //= 10
        return ls


# @lc code=end
