class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        length = len(word)
        m, n = len(board), len(board[0])
        dirs = [0,1],[0,-1],[1,0],[-1,0]
        def dfs(cx:int, cy:int, pos:int, visited:set) -> bool:
            if pos == length:
                return True

            visited.add((cx,cy))
            for d in dirs:
                nx, ny = cx + d[0], cy + d[1]
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                if board[nx][ny] != word[pos] or (nx, ny) in visited:
                    continuew
                if dfs(nx, ny, pos + 1, visited):
                    return True

            visited.remove((cx,cy))
                
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    res = dfs(i,j,1, set())
                    if res:
                        return True

        return False