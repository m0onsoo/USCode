# https://leetcode.com/problems/spiral-matrix/
# 54-spiral-matrix


# Brute force:
# while m > 0 and n > 0
# go right until i == n-1
# when i == n-1 : go down until j == m -1
# when j == m-1 : go left until i == 0
# when i == 0 : m = m - 1, go up until j == 0
# when j == 0 : restart. go right until i == n-1
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        l_rows, l_cols = 0, 0
        reached_right, reached_bottom = False, False
        ans = []

        i, j = 0, 0
        while l_rows < rows and l_cols < cols:
            if not reached_right and not reached_bottom:
                while j < cols - 1:
                    ans.append(matrix[i][j])
                    j += 1
                l_rows += 1
                reached_right = True
            elif reached_right and not reached_bottom:
                while i < rows - 1:
                    ans.append(matrix[i][j])
                    i += 1
                cols -= 1
                reached_bottom = True
            elif reached_right and reached_bottom:
                while j > l_cols:
                    ans.append(matrix[i][j])
                    j -= 1
                rows -= 1
                reached_right = False
            elif not reached_right and reached_bottom:
                while i > l_rows:
                    ans.append(matrix[i][j])
                    i -= 1
                l_cols += 1
                reached_bottom = False
        ans.append(matrix[i][j])
        return ans
