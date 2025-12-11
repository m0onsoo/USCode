# https://leetcode.com/problems/word-search/
# 79-word-search


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        ans = False

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c, remaining):
            if not (0 <= r < rows and 0 <= c < cols):
                return False
            if visited[r][c] == True:
                return False
            if remaining[0] != board[r][c]:
                return False
            if len(remaining) == 1:
                return True

            ans = False
            if remaining[0] == board[r][c]:
                visited[r][c] = True
                for dr, dc in dirs:
                    ans = ans or dfs(r + dr, c + dc, remaining[1:])
                visited[r][c] = False
            return ans

        final_ans = False
        for i in range(rows):
            for j in range(cols):
                if word[0] == board[i][j]:
                    final_ans = final_ans or dfs(i, j, word)

        return final_ans
