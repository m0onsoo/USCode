from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for string in strs:
            key_ = ''.join(sorted(string))
            
            anagrams[key_].append(string)
            

        return list(anagrams.values())