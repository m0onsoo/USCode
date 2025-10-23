class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        results = []
        self.findRecursively(0, s, wordDict, results, [])
        return results

    def findRecursively(self, sp: str, s: str, wordDict: List[str], 
        results:List[str], current_sentence:List[str]) -> None:
        if sp >= len(s):
            results.append(" ".join(current_sentence))
            return
        
        for i in range(sp+1, len(s)+1):
            subset = s[sp:i]
            if subset in wordDict:
                current_sentence.append(subset)
                self.findRecursively(i, s, wordDict, results, current_sentence)
                current_sentence.pop()

                
