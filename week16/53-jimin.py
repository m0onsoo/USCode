# https://leetcode.com/problems/maximum-subarray/
# 53-maximum-subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        n = len(nums)
        l = 0
        max_sum = 0
        cur_sum = 0

        if max(nums) < 0:
            return max(nums)

        for r, num in enumerate(nums):
            cur_sum += num

            if cur_sum < 0:
                cur_sum = 0
            else:
                max_sum = max(max_sum, cur_sum)

        return max_sum


# 1pass sol
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 초기값을 아주 작은 수 혹은 첫 번째 원소로 잡습니다.
        max_sum = nums[0] 
        cur_sum = 0

        for num in nums:
            cur_sum += num
            
            # 1. 갱신: 현재까지의 합이 최대인지 확인
            max_sum = max(max_sum, cur_sum)
            
            # 2. 리셋: 합이 음수가 되면 "버리고" 0부터 다시 시작
            # (다음 숫자를 위해 0으로 만드는 것일 뿐, max_sum은 이미 위에서 안전하게 저장됨)
            if cur_sum < 0:
                cur_sum = 0
                
        return max_sum