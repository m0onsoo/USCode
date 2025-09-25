from typing import List

class Solution:
    # 3ms, 18.55MB
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                # if sum of two numbers is same with target
                return [l + 1, r + 1]