# https://leetcode.com/problems/word-break/description/
# 139-word-break

# 1. Brute Force :
## loop for the word Dict and s
## check the char pos that is found


# 2. DP
## i is 0~i chars
## dp[i] = dp[0:i-len(word)] && dp[i-word:i+1] if possible for all word


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True

        # Base cases
        for word in wordDict:
            if s[: len(word)] == word:
                dp[len(word)] = True

        for i in range(1, len(s) + 1):  # outer loop : len(s)
            for word in wordDict:  # inner loop : len(wordDict)
                if i >= len(word):
                    if dp[i] == False:
                        dp[i] = dp[i - len(word)] and s[i - len(word) : i] == word
        return dp[len(s)]
