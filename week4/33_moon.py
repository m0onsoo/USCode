from typing import List

# 0ms, 18.4MB
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            # handle edge case
            return 0 if nums[0] == target else -1

        left, right = nums[0], nums[-1]

        # first, find the max index and number using modified binary search
        max_idx = self.FindMaxIndex(nums)
        max_num = nums[max_idx]

        if max_num == target:
            # if target is same with max, return max index
            return max_idx
        elif left <= target and target < max_num:
            # if left <= target < max_num, search the target from left side of nums
            return self.BinarySearch(nums[:max_idx], target)
        elif nums[(max_idx + 1) % len(nums)] <= target and target <= right:
            # if min_num <= target <= right, search the target from the right side of nums
            flag = self.BinarySearch(nums[max_idx+1:], target)
            if flag == -1:
                # if target number is not in the subarray
                return -1

            # resulted index(flag) + (max_idx+1)
            return max_idx+1 + flag
        else:
            # if target number is out of range(min, max)
            return -1



    def FindMaxIndex(self, arr: List[int]) -> int:
        if len(arr) < 1:
            return 0
        if len(arr) == 2:
            # when the size of array reduced to 2, we can find max number in O(1)
            return arr.index(max(arr))
        
        mid = int(len(arr) / 2)
        if arr[0] < arr[mid]:
            # left < mid
            return mid + self.FindMaxIndex(arr[mid:])
        else:
            # mid <= right
            return self.FindMaxIndex(arr[:mid])

    def BinarySearch(self, arr: List[int], target: int) -> bool:
        if len(arr) < 1:
            # when the array is empty
            return -1
        
        mid = int(len(arr) / 2)
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            flag = self.BinarySearch(arr[:mid], target)
            if flag == -1:
                return -1
            return flag
        else:
            flag = self.BinarySearch(arr[mid+1:], target)
            if flag == -1:
                return -1
            return mid+1 + flag


        