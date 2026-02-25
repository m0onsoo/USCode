from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # [2, 3, 3], target = 6
        num2indices = defaultdict(list)
        for i, num in enumerate(nums):
            num2indices[num].append(i)
        
        answer = []
        nums.sort()
        l, r = 0, len(nums) - 1
        while l < r:
            cur_sum = nums[l] + nums[r]
            if cur_sum == target:
                answer.append(num2indices[nums[l]].pop())
                answer.append(num2indices[nums[r]].pop())

                # 바로 종료 혹은 l += 1, r -= 1
                return answer
            elif cur_sum < target:
                l += 1
            else:
                r -= 1
        
        return answer
