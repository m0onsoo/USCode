class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])

        res = []
        cnt, target = 0, m * n
        i, j = 0, -1
        
        left, right = 0, n - 1
        top, down = 1, m - 1
        
        while i <= down and j <= right and cnt < target:
            while j < right and cnt < target:
                j += 1
                res.append(matrix[i][j])
                cnt += 1
            right -= 1

            while i < down and cnt < target:
                i += 1
                res.append(matrix[i][j])
                cnt += 1
            down -= 1

            while j > left and cnt < target:
                j -= 1
                res.append(matrix[i][j])
                cnt += 1
            left += 1
            
            while i > top and cnt < target:
                i -= 1
                res.append(matrix[i][j])
                cnt += 1
            top += 1
        
        return res