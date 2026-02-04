# https://leetcode.com/problems/subarray-sum-equals-k/
# 560-subarray-sum-equals-k

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        sub_sum = 0
        prev_sum = defaultdict(int)
        
        ans = 0
        for num in nums:
            sub_sum += num
            need = sub_sum - k
            ans += prev_sum[need]
            if sub_sum == k:
                ans += 1
            prev_sum[sub_sum] += 1

        return ans