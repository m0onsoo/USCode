# https://leetcode.com/problems/valid-sudoku/
# 36-valid-sudoku

# Idea :
# 1. Brute Force
## scan thru all row to see non duplicate
## same for column, and 3*3 box
## this will lead to three all-scans

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row, col = len(board), len(board[0])

        for r in range(row):
            count = [0] * 9
            for c in range(col):
                if board[r][c].isnumeric():
                    count[int(board[r][c]) - 1] += 1
                    if count[int(board[r][c]) - 1] > 1:
                        # print("row")
                        return False

        
        for c in range(col):
            count = [0] * 9
            for r in range(row):
                if board[r][c].isnumeric():
                    count[int(board[r][c]) - 1] += 1
                    if count[int(board[r][c]) - 1] > 1:
                        # print("col")
                        return False

        for i in range(3):
            for j in range(3):
                count = [0] * 9
                for r in range(3 * i, 3 * (i + 1)):
                    for c in range(3 * j, 3 * (j + 1)):
                        if board[r][c].isnumeric():
                            count[int(board[r][c]) - 1] += 1
                            if count[int(board[r][c]) - 1] > 1:
                                # print("box")
                                # print(i, j)
                                # print(count)
                                return False
        return True