import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums.sort(reverse = True)
        # return nums[k-1]

        # O(n)
        # for i, num in enumerate(nums):
        #     nums[i] = [-num, num]
        heapq.heapify(nums)

        # O(nlogn)
        for _ in range(len(nums) - k + 1):
            n = heapq.heappop(nums)
        
        return n