from typing import List

class Solution:
    # 583ms, 20.74MB
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        nums.sort() # O(nlogn)

        results = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                # if we visit same element again, it will make a duplicate triplet
                # add condition 'i > 0' because of counter example [0, 0, 0]. This Conditional Statement does not intend to compare 0th index and -1th(last) index
                continue
            
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum_ = nums[i] + nums[left] + nums[right]
                if sum_ == 0:
                    results.append([nums[i], nums[left], nums[right]])

                    # we don't need duplicate triplets, so move until adjacent elements are not same
                    # e.g. [-1, -1, -1, -1, -1, 2, 2, 2]
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right - 1] == nums[right]:
                        right -= 1

                    # once elements satisfy the condition, pointers need to move
                    left += 1
                    right -= 1

                elif sum_ < 0:
                    left += 1
                else:
                    # if sum_ > 0
                    right -= 1
        
        return results
