from typing import List

""" Time Limit Exceeded with Brute Force approach """

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        flag = False
        # print(s)
    
        for i in range(len(s)-1, -1, -1):
            if s[i:] in wordDict: # if s[i:] in Opt solution
                if i == 0:
                    # print("IN:",s[i:])
                    # print(s)
                    flag = True
                else:
                    # print(i, s[i:len(s)-1])
                    flag = self.wordBreak(s[:i], wordDict) or flag
            
            if flag == True:
                return flag

        return flag


        