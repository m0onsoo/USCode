# 15ms, 17.6MB

from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        def dfs_recursive(r, c, curr):
            if r < 0 or r >= m or c < 0 or c >= n:
                # index out of range
                return 0
            
            if grid[r][c] == 0 or grid[r][c] == 2:
                # not island or already visited
                return 0
            
            else:
                grid[r][c] = 2        # 2: visited
                for dr, dc in dirs:
                    curr = max(curr, dfs_recursive(r+dr, c+dc, curr+1))
            return curr

        def dfs_stack(sr: int, sc: int):
            grid[sr][sc] = 2     # visited
            stack = [(sr, sc)]

            res = 0
            while stack:
                top = stack.pop()
                r, c = top[0], top[1]
                res += 1

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2         # visited
                        stack.append((nr, nc))
            
            return res

        def bfs(sr: int, sc: int):
            grid[sr][sc] = 2
            queue = deque()
            queue.append((sr, sc))

            res = 0
            while queue:
                island = queue.popleft()
                r, c = island[0], island[1]
                res += 1

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2      # visited
                        queue.append((nr, nc))
            return res



        
        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    # 1. dfs recursive
                    # curr = dfs_recursive(r, c, 1)
                    # res = max(res, curr)

                    # 2. dfs stack
                    # curr = dfs_stack(r, c)
                    # res = max(res, curr)

                    # 3. bfs
                    curr = bfs(r, c)
                    res = max(res, curr)

        return res