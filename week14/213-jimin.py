# https://leetcode.com/problems/house-robber-ii/
# 213-house-robber-ii
# used hint

# DP[i,j] =  max(dp[i,j-1], dp[i+1,j])


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        dp_0 = [0] * n  # 0~n-1
        dp_0[0], dp_0[1] = nums[0], max(nums[0], nums[1])

        dp_1 = [0] * n  # 1~n
        dp_1[0], dp_1[1] = 0, nums[1]

        for i in range(2, n):
            # dp_0 로직: 마지막 집(n-1)인 경우에는 털지 않고 이전 값 유지
            if i == n - 1:
                dp_0[i] = dp_0[i - 1]
            else:
                dp_0[i] = max(dp_0[i - 1], dp_0[i - 2] + nums[i])

            # dp_1 로직: 마지막 집까지 정상적으로 고려
            dp_1[i] = max(dp_1[i - 1], dp_1[i - 2] + nums[i])

        # 두 경우 중 최댓값 반환
        return max(dp_0[n - 1], dp_1[n - 1])
