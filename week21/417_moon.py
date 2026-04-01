class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        pacifics, atlantics = set(), set()

        def BFS(r: int, c: int) -> bool:
            pacific, atlantic = False, False
            visited = set()

            queue = deque([(r, c)])
            while queue:
                r, c = queue.popleft()
                if r == 0 or c == 0 or (r, c) in pacifics:
                    pacific = True
                    pacifics.add((r, c))
                if r == m - 1 or c == n - 1 or (r, c) in atlantics:
                    atlantic = True
                    atlantics.add((r, c))
                if pacific and atlantic:
                    return True

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and \
                        (nr, nc) not in visited and heights[nr][nc] <= heights[r][c]:
                        visited.add((nr, nc))
                        queue.append((nr, nc))

            return pacific and atlantic

        result = []
        for r in range(m):
            for c in range(n):
                if BFS(r, c):
                    result.append([r, c])
        return result