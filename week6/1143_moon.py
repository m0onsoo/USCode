class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2)+1) for _ in range(len(text1)+1)]

        l1, l2 = len(text1), len(text2)

        for i in range(1, l1+1):
            for j in range(1, l2+1):
                if text1[i-1] == text2[j-1]:
                    # if current pointer(i, j) belongs to OPT(i, j), then add 1 to OPT(i-1, j-1)
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    # else OPT(i, j) is either OPT(i-1, j) or OPT(i, j-1)
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])

        
        return dp[l1][l2]
