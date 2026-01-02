from collections import defaultdict

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        dict_ = defaultdict(int)
        for n in nums:
            dict_[n] += 1
        
        for key, val in dict_.items():
            if val >= 2:
                return key