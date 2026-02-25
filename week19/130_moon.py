from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        m, n = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        VISITED = set() # global visited set for all regions

        def isSurrounded(r: int, c: int) -> bool:
            if r == 0 or r == m - 1 or c == 0 or c == n - 1:
                return False
            else:
                return True

        def BFS(r: int, c: int):
            surrounded = isSurrounded(r, c) # initialized True if region is surrounded else False

            # find all region
            visited = set([(r, c)])      # local visited set for current region
            VISITED.add((r, c))
            queue = deque([(r, c)])

            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'O' and (nr, nc) not in VISITED:
                        visited.add((nr, nc))
                        VISITED.add((nr, nc))
                        queue.append((nr, nc))

                        # update surrounded status
                        # if we met False even one time, it will remain False
                        surrounded = surrounded and isSurrounded(nr, nc)
            
            if surrounded:
                # if region is sorrounded, we need to replace all 'O' -> 'X' in-place
                for r, c in visited:
                    board[r][c] = 'X'


        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O' and (r, c) not in VISITED:
                    # run BFS
                    BFS(r, c)



