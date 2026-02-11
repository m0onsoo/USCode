# 0ms, 27.84MB
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums) - 1
        
        def binary_search(l, r):
            mid = (l + r) // 2
            if l > r:
                return -1

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return binary_search(mid + 1, r)
            else:
                return binary_search(l, mid - 1)

        return binary_search(0, n)