class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        m,n,t = len(grid), len(grid[0]),0
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j))

        while queue:
            next_list = []
            for orange in queue:
                sr, sc = orange[0], orange[1]
                # print(orange)
                
                for d in dirs:
                    nr,nc = sr + d[0], sc + d[1]
                    if nr >= m or nr < 0 or nc >= n or nc < 0 or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    next_list.append((nr,nc))
            
            if next_list:
                queue = deque(next_list)
                t += 1
            else:
                break

        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        
        return t

        