class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_idx = 0
        last_idx = len(nums) - 1
        
        for i, jump in enumerate(nums):
            if i > max_idx:
                return False
            
            max_idx = max(max_idx, i + jump)

            if max_idx >= last_idx:
                return True



        """
        last_index = len(nums) - 1

        def jump(index):
            # print(index)
            if index > last_index:
                return False
            if index == last_index:
                return True

            flag = False
            for j in range(nums[index], 0, -1):
                flag = flag or jump(index + j)
            
            return flag

        return jump(0)
        """

