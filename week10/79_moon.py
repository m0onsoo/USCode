class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = []

        def dfs(search, x, y):
            if x < 0 or x >= n or y < 0 or y >= m or (x, y) in visited:
                # index out of range
                # if (x, y) is already visited
                return False
            
            # append current char and coordinates
            search.append(board[y][x])
            visited.append((x, y))
            # print((x, y), search)

            curr_word = ''.join(search)
            if curr_word == word:
                # if current word matches word
                # print((x, y), curr_word)
                return True

            if board[y][x] == word[len(curr_word)-1]:
                # only part matches
                flag = dfs(search, x+1, y) or dfs(search, x-1, y) or dfs(search, x, y+1) or dfs(search, x, y-1)

                search.pop()
                visited.remove((x, y))

                return flag
            else:
                # dont't match -> prune (back)
                search.pop()
                visited.remove((x, y))
                return False

        
        for y in range(m):
            for x in range(n):
                result = dfs([], x, y)

                if result:
                    # print((x, y), result)
                    return True

        return False
            


"""
Time Limit Exceeded Error

board =
[["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "B", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"]]

word =
"AB"
"""