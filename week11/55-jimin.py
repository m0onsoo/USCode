# https://leetcode.com/problems/jump-game/
# 55-jump-game
class Solution:
    # Timeout
    def canJump(self, nums: List[int]) -> bool:
        # DP[i] : can I come here?
        if len(nums) <= 1:
            return True

        DP = [0] * len(nums)
        DP[0] = 1

        for i in range(len(nums)):
            if DP[i] != 0:
                for j in range(nums[i] + 1):
                    if i + j < len(nums):
                        DP[i + j] = 1
                    if i + j > len(nums):
                        break

        return True if DP[len(nums) - 1] == 1 else False

    def canJump(self, nums: List[int]) -> bool:
        # DP[i] : max jumps left
        n = len(nums)

        if len(nums) <= 1:
            return True

        DP = [0] * len(nums)
        DP[0] = nums[0]

        for i in range(1, len(nums)):
            if DP[i - 1] != 0:
                DP[i] = max(DP[i - 1] - 1, nums[i])
        print(DP)
        return True if DP[n - 2] != 0 else False
