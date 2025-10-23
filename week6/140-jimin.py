# https://leetcode.com/problems/word-break-ii/


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        def helper(string):
            if not string:
                return ""

            for i in range(1, len(string) + 1):
                prefix = string[:i]
                if prefix in wordDict:
                    rest = helper(string[i:])
                    if rest is not None:
                        if rest == "":
                            return prefix
                        else:
                            return prefix + " " + rest

            return None

        candidate = []
        for i in range(len(s)):
            if s[0:i] in wordDict:
                candidate.append(s[0:i] + " " + helper(s[i:]))

        print(candidate)
