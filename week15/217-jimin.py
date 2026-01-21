# https://leetcode.com/problems/contains-duplicate/description/
# 217-contains-duplicate


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False
