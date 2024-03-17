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
        n *= n
        matrix = [[n]]
        i = n - 1
        while i > 0:
            row = []
            for j in range(len(matrix[0])):
                row.append(i)
                i -= 1
            matrix.append(row)
            matrix = [row[::-1] for row in list(map(list, zip(*matrix)))]

        matrix = [row[::-1] for row in list(map(list, zip(*matrix)))]
        return matrix


# @lc code=end
