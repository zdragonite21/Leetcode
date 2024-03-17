#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#


# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        ans = matrix.pop(0)
        ## transpose and reverse to get the next section to pop
        matrix = [*map(list, zip(*matrix))][::-1]
        return ans + self.spiralOrder(matrix)


# @lc code=end
