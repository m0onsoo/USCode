# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# 167-two-sum-ii-input-array-is-sorted

# Idea
# 1. brute force
## nested loop => O(n^2)

# 2. use hash set
## store complement[target - number[n]] = n
## store as tuple, with index stored
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         comp = {target - num : (float('inf'), i + 1) for i, num  in enumerate(numbers)}

#         print(comp)
#         for i, num in enumerate(numbers):
#             if num in comp and comp[num][0] != float('inf'):
#                 return [comp[num][1], i + 1]
#             else:
#                 comp[target - num] = (num, i + 1)


# 3. two pointer
## use left and right.
## if small increase left
## if big decrease right


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            temp_sum = numbers[l] + numbers[r]
            if temp_sum == target:
                return [l + 1, r + 1]
            elif temp_sum > target:
                r -= 1
            elif temp_sum < target:
                l += 1
