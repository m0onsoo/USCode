# https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/
# 215-kth-largest-element-in-an-array


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-x for x in nums]
        heapq.heapify(heap)

        ans = 0
        for i in range(k):
            ans = heapq.heappop(heap)

        return -ans

    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)

        for x in nums[k:]:
            if x > heap[0]:
                heapq.heapreplace(heap, x)
        return heap[0]
