#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#


# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        print(matrix[~1])

        def dfs(i, n):
            if n == 1:
                return
            j = i + n - 1
            for k in range(j - i):
                (
                    matrix[i][i + k],
                    matrix[i + k][j],
                    matrix[j][j - k],
                    matrix[j - k][i],
                ) = (
                    matrix[j - k][i],
                    matrix[i][i + k],
                    matrix[i + k][j],
                    matrix[j][j - k],
                )
            if n == 2:
                return
            dfs(i + 1, n - 2)

        dfs(0, len(matrix))


# @lc code=end
