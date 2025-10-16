### 1. 단어 길이 먼저 측정 후 lens = {len(w) for w in wordDict}에 저장
### 2. 그 길이만큼 확인
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        if not word_set:
            return False

        # 단어 길이 만큼 먼저 확인
        lens = set(len(w) for w in word_set)

        # dp[i] = s[:i]가 원래 단어들로 완전 분해 가능하면 True
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for L in lens:
                if L <= i and dp[i - L] and s[i - L:i] in word_set:
                    dp[i] = True
                    break  # 이미 True면 더 볼 필요 없음

        return dp[n]