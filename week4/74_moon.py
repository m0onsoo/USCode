from typing import List

# 0ms, 18.29MB
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = []
        # extend all row in matrix: O(m)
        for row in matrix:
            arr.extend(row)
        
        # Binary search takes O(log(m*n))
        return self.BinarySearch(arr, target)

    
    def BinarySearch(self, arr: List[int], target: int):
        if len(arr) < 1:
            # if array is empty
            return False

        mid = int(len(arr) / 2)
        if target == arr[mid]:
            return True
        elif target < arr[mid]:
            # left side
            return self.BinarySearch(arr[:mid], target)
        else:
            # right side
            return self.BinarySearch(arr[mid+1:], target)