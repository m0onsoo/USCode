from collections import deque, defaultdict

# 39ms, 21.98MB
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1  
        curr_sum = 0
        ans = 0
        
        for num in nums:
            curr_sum += num
            
            # (현재 누적합 - k)가 이전에 등장한 적이 있는지 확인
            # 등장한 횟수만큼 정답에 더함
            if (curr_sum - k) in count:
                ans += count[curr_sum - k]
            
            # 현재 누적합을 카운트에 저장
            count[curr_sum] += 1
            
        return ans