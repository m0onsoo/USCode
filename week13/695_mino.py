class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        m,n = len(grid), len(grid[0])
        visited = set()

        def bfs(i:int, j:int)->int:
            queue = deque()
            queue.append((i,j))
            visited.add((i,j))
            area = 0
            dirs = [(0,1),(1,0),(0,-1),(-1,0)]
            while queue:
                r, c = queue.popleft()
                area += 1

                for d in dirs:
                    nr, nc = r + d[0], c + d[1]
                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue
                    if grid[nr][nc] == 0 or (nr, nc) in visited:
                        continue
                    queue.append((nr,nc))
                    visited.add((nr,nc))
            return area

        for i in range(m):
            for j in range(n):
                if grid[i][j] and (i,j) not in visited:
                    area = bfs(i,j)
                
                    if area > max_area:
                        max_area = area
                
        return max_area