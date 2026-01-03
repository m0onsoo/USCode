class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l, r = 0, 0
        while True:
            l = nums[l]
            r = nums[nums[r]]
        
            if l == r:
                break

        ll = 0
        while l != ll:
            l = nums[l]
            ll = nums[ll]

        return l
        
            