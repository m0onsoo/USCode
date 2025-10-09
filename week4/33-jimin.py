# https://leetcode.com/problems/search-a-2d-matrix/
# 74-search-a-2d-matrix


# Brute force:
## search all - n^2

# Optimize
## attatch all rows into one row


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        if not matrix or not matrix[0]:
            return False

        array = []
        left = 0
        right = rows * cols - 1
        while left <= right:
            mid = (left + right) // 2
            r = mid // cols
            c = mid % cols
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                right = mid - 1
            elif matrix[r][c] < target:
                left = mid + 1
        return False
