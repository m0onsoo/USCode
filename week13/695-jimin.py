# https://leetcode.com/problems/max-area-of-island/
# 695-max-area-of-island


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            if not 0 <= r < rows or not 0 <= c < cols:
                return 0
            if grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            area = dfs(r + 1, c) + dfs(r, c + 1) + dfs(r - 1, c) + dfs(r, c - 1) + 1
            return area

        ans = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    ans = max(dfs(i, j), ans)

        return ans
