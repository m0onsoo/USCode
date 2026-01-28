class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alphabets = [0] * (ord('z') - ord('a') + 1)

        if len(s) != len(t):
            return False

        for s_ch, t_ch in zip(s, t):
            alphabets[ord(s_ch) - ord('a')] += 1
            alphabets[ord(t_ch) - ord('a')] -= 1

        for cnt in alphabets:
            if cnt != 0:
                return False

        return True
        