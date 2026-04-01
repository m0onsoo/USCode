# https://leetcode.com/problems/pacific-atlantic-water-flow/
# 417-pacific-atlantic-water-flow

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        rows, cols = len(heights), len(heights[0])

        pacific = [[False] * cols for _ in range(rows)]
        atlantic = [[False] * cols for _ in range(rows)]

        # 각각 pacific, atlantic이랑 맞닿은 놈들이 거꾸로 어디까지 올라갈 수 있나 해보면 어떤가?

        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        # Pacific
        q = deque([])

        for i in range(rows):
            for j in range(cols):
                if i == 0 or j == 0:
                    q.append((i, j))

        while q:
            r,c = q.popleft()
            pacific[r][c] = True

            for dr, dc in dirs:
                nr, nc = dr +r , dc + c
                if 0 <= nr < rows and 0<= nc < cols and heights[r][c] <= heights[nr][nc] and not pacific[nr][nc]:
                    q.append((nr,nc))
        # Atlantic
        q = deque([])

        for i in range(rows):
            for j in range(cols):
                if i == rows-1 or j == cols-1:
                    q.append((i, j))

        while q:
            r,c = q.popleft()
            atlantic[r][c] = True

            for dr, dc in dirs:
                nr, nc = dr +r , dc + c
                if 0 <= nr < rows and 0<= nc < cols and heights[r][c] <= heights[nr][nc] and not atlantic[nr][nc]:
                    q.append((nr,nc))


        res = []
        for i in range(rows):
            for j in range(cols):
                if pacific[i][j] == atlantic[i][j] == True:
                    res.append([i, j])

        return res