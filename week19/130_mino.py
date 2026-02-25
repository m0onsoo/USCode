class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        visited = set()
        dirs = [(0,-1),(0,1),(1,0),(-1,0)]
        def bfs(i, j):
            queue = deque()
            queue.append((i, j))
            visited.add((i, j))
            while queue:
                    cr, cc = queue.pop()
                    for d in dirs:
                        nr, nc = cr + d[0], cc + d[1]
                        if nr < 0 or nr >= m or nc < 0 or nc >= n:
                            continue
                        if board[nr][nc] == 'X' or (nr, nc) in visited:
                            continue
                        queue.append((nr, nc))
                        visited.add((nr, nc))

        for i in range(m):
            if board[i][0] == 'O' and (i,0) not in visited:
                bfs(i, 0)
            if board[i][n-1] == 'O' and (i,n-1) not in visited:
                bfs(i, n-1)

        for j in range(n):
            if board[0][j] == 'O' and (0,j) not in visited:
                bfs(0, j)
                    
            if board[m-1][j] == 'O' and (m-1, j) not in visited:
                bfs(m-1, j)

        # print(visited)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i, j) not in visited:
                    board[i][j] = 'X'