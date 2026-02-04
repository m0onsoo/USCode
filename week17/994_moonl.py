from collections import deque

# 3ms, 19.4MB
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        queue = deque()
        cnt = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    cnt += 1

        if len(queue) == 0 and cnt == 0:
            # if there is no fresh and rotten orange
            return 0

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        minute = -1
        while queue:
            # print(minute, queue)
            minute += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        cnt -= 1
        
        return minute if cnt == 0 else -1

