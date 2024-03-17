#
# @lc app=leetcode id=59 lang=python
#
# [59] Spiral Matrix II
#


# @lc code=start
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = []
        lo = n * n + 1
        while lo > 1:
            hi = lo
            lo = lo - len(matrix)
            row = [range(lo, hi)]
            matrix = row + zip(*matrix[::-1])
        print(matrix)
        return matrix


# @lc code=end
