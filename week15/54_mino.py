class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dirs = [[0,1], [1,0], [0,-1],[-1,0]]
        x, y, curr = 0, 0, 0
        m, n = len(matrix), len(matrix[0])
        board = [[False for _ in range(n)] for _ in range(m)]
        cnt = 0
        res = []
        while True:
            if not board[x][y]:
                board[x][y] = True
                res.append(matrix[x][y])
                cnt += 1
            
            if cnt == m*n:
                break    

            nx = x + dirs[curr][0]
            ny = y + dirs[curr][1]

            if nx >= m or ny >= n or board[nx][ny]:
                curr = (curr + 1) % 4
            else:
                x = nx
                y = ny

        return res
