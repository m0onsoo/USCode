from collections import deque, defaultdict

# 18ms, 17.76MB
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Worst Case: (n-1) + (n-1) = O(n)

        window = deque()
        count = defaultdict(int)
        current_max = 0
        for idx, char in enumerate(s):
            # insert element into window and count
            window.append(char)
            count[char] += 1

            if count[char] > 1:
                # if there is a duplication, update the maximum window size and remove the duplication

                # calcalate the window size except the latest element
                current_max = max(current_max, len(window) - 1)
                while window and window[0] != char:
                    # remove elements until we find duplicate number
                    pop_char = window.popleft()
                    count[pop_char] -= 1
                
                # remove duplication
                window.popleft()
                count[char] -= 1
        
        # we need to check if the last window is the maximum size
        current_max = max(current_max, len(window))

        return current_max
            