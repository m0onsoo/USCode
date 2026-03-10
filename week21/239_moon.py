class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()

        for idx, num in enumerate(nums):
            while q and q[-1] < num:
                q.pop()
            q.append(num)

            if idx >= k and nums[idx - k] == q[0]:
                q.popleft()
            
            if idx >= k - 1:
                res.append(q[0])
        
        return res


"""
# TLE Solution:

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        
        # res = []
        # for i in range(n - k + 1):
        #     window = nums[i: i + k]

        #     res.append(max(window))
        
        res = []
        window = deque()
        max_num = nums[0]
        for i in range(n):
            # print(window, max_num)
            if len(window) < k:
                # O(1)
                window.append(nums[i])
                max_num = max(max_num, nums[i])
            else:
                # res array update
                res.append(max_num)

                # update sliding window
                pop = window.popleft()
                window.append(nums[i])

                # update max_num
                if nums[i] > max_num:
                    max_num = nums[i]
                elif pop == max_num:
                    # O(k)
                    max_num = max(window)
        res.append(max_num)
        
        return res

"""