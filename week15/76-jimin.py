# https://leetcode.com/problems/minimum-window-substring/
# 76-minimum-window-substring

class Solution:

    # My sol : did not pass..

    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        # if size of t is smaller than s: return ""
        if m < n:
            return ""

        count_t = Counter(t)
        count_s = Counter([])

        # l =  0

        # for r in range(len(t), m):
        
        l = 0
        min_len = float('inf')
        ans = ""

        required = len(count_t.values())


        for r, char in enumerate(s):
            if char in count_t:
                count_s[char] += 1
                print(char)
            while (count_s[char] > count_t[char] or s[l] not in count_t) and l < r:
                if s[l] in count_t:
                    print("minus ", s[l])
                    count_s[s[l]] -= 1
                l += 1
            if count_s == count_t:
                print(s[l:r+1], l, r)
                if min_len > r - l + 1:
                    ans = s[l:r+1]
                    min_len = r-l+1
        
        return ans

    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        if len(s) < len(t):
            return ""

        need = Counter(t)
        window = defaultdict(int)

        required = len(need)
        formed = 0

        l = 0
        best_len = float("inf")
        best_l = 0

        for r, char in enumerate(s):
            if char in need:
                window[char] += 1
                if window[char] == need[char]:
                    formed += 1
            
            while formed == required:
                if r - l + 1 < best_len:
                    best_len = r-l+1
                    best_l = l

                left_ch = s[l]
                if left_ch in need:
                    window[left_ch] -= 1
                    if window[left_ch] < need[left_ch]:
                        formed -= 1
                l += 1

            
        return "" if best_len == float('inf') else s[best_l:best_l + best_len]
