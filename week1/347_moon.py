from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counts = Counter(nums)
        results = [num for num, _ in num_counts.most_common(k)] # most_common은 (num, frequnecy) 튜플 반환

        return results