class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # edge case
        if not word1 and not word2:
            return 0
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)

        # base case
        ## 0,0 = 0
        dp = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        for i in range(1, len(word1) + 1):
            dp[i][0] = i
            for j in range(1, len(word2) + 1):
                dp[0][j] = j

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:  # if same char
                    dp[i][j] = dp[i - 1][j - 1]
                # elif i > j:  # Delete
                #     dp[i][j] = dp[i-1][j] + 1
                # elif i < j:  # Insert
                #     dp[i][j] = dp[i][j-1] + 1
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

        # for i in range(len(word1) + 1):
        #     print(dp[i])
        return dp[len(word1)][len(word2)]
