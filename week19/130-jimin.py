# https://leetcode.com/problems/surrounded-regions/
# 130-surrounded-regions

class Solution:
    # def solve(self, board: List[List[str]]) -> None:
    #     """
    #     Do not return anything, modify board in-place instead.
    #     """
    #     rows, cols = len(board), len(board[0])

    #     dirs = [(1,0), (-1,0), (0,1), (0,-1)]


    #     def dfs(r,c):
    #         if not 0 <= r < rows or not 0 <= c < cols:
    #             return False
    #         if board[r][c] == "X" or board[r][c] == "V":
    #             return True
    #         board[r][c] = "V" #visiting
    #         isSurrounded = True
    #         for dr, dc in dirs:
    #             nr, nc = dr + r, dc + c
    #             isSurrounded = isSurrounded and dfs(nr,nc)
    #         if isSurrounded:
    #             board[r][c] = "X"
    #         else:
    #             board[r][c] = "O" #visiting end
    #         return isSurrounded


    #     for i in range(rows):
    #         for j in range(cols):
    #             dfs(i,j)

    #     return board

        def solve(self, board: List[List[str]]) -> None:
            rows, cols = len(board), len(board[0])

            dirs = [(1,0), (-1,0), (0,1), (0,-1)]


            def dfs_safe(r,c):
                if not 0 <= r < rows or not 0 <= c < cols:
                    return
                if board[r][c] == "X" or board[r][c] == "S":
                    return
                board[r][c] = "S"
                for dr, dc in dirs:
                    nr, nc = dr + r, dc + c
                    dfs_safe(nr, nc)

            def dfs_surr(r,c):
                if not 0 <= r < rows or not 0 <= c < cols:
                    return
                if board[r][c] == "S" or board[r][c] == "X":
                    return
                board[r][c] = "X"
                for dr, dc in dirs:
                    nr, nc = dr + r, dc + c
                    dfs_surr(nr, nc)

            for i in range(rows):
                for j in range(cols):
                    if i == 0 or i == rows-1 or j == 0 or j == cols-1:
                        dfs_safe(i,j)
                        
            for i in range(rows):
                for j in range(cols):
                    dfs_surr(i,j)

            for i in range(rows):
                for j in range(cols):
                    if board[i][j] == "S":
                        board[i][j] = "O"
            return board