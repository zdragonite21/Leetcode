#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#
from collections import Counter


# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if any(y > 1 for x, y in Counter(row).items() if x != "."):
                return False

        for col in zip(*board):
            if any(y > 1 for x, y in Counter(col).items() if x != "."):
                return False

        for i in range(3):
            for j in range(3):
                c = Counter(
                    [y for x in board[i * 3 : i * 3 + 3] for y in x[j * 3 : j * 3 + 3]]
                )
                if any(y > 1 for x, y in c.items() if x != "."):
                    return False

        return True


# @lc code=end
