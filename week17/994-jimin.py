# https://leetcode.com/problems/rotting-oranges/
# 994-jimin


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        oranges = 0
        q = deque([])
        mins = -1
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1: # count fresh
                    oranges += 1 
                elif grid[i][j] == 2: 
                    q.append((i,j))

        dirs = [(1,0), (0,1), (-1,0), (0,-1)]

        if oranges == 0:
            return 0
            
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        oranges -= 1
                        q.append((nr,nc))
            mins += 1
        if oranges > 0:
            return -1

        return mins