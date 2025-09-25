import heapq
from typing import List

class Solution:
    # 431 ms, 38.63MB
    def maxArea(self, height: List[int]) -> int:
        # initialzie an array for heap structrue
        heap = []

        for i, h in enumerate(height):
            # it takes O(nlogn) to build a heap using heap push
            heapq.heappush(heap, (-h, i))
        
        # extract two top nodes for initial left and right pointer
        left = heapq.heappop(heap)
        right = heapq.heappop(heap) # tuple. 0th is height(shoud be abs) and 1th is index

        if abs(left[1]) > abs(right[1]):
            left, right = right, left

        # calculate initial amount of water
        stored = (right[1] - left[1]) * min(abs(left[0]), abs(right[0]))

        while heap:
            # extract node with max height
            root = heapq.heappop(heap)

            idx = root[1]
            # update left and right pointer w.r.t. root's loacation
            if idx < left[1]:
                # if idx locates left than previous left index, we need to update left
                left = root
            elif right[1] < idx:
                right = root
            else:
                # left[1] < idx and idx < right[1]
                # if idx is between left and right, you don't need to anything
                continue
            
            # calculate current amount of water
            water = (right[1] - left[1]) * min(abs(left[0]), abs(right[0]))
            # update maximum amount of water
            stored = max(stored, water)
        
        return stored