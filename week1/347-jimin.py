# https://leetcode.com/problems/top-k-frequent-elements/
# 347-top-k-frequent-elements
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

# Idea :
# 1. Brute Force
## put it all in a set, count
## sort the set
## print

from collections import Counter

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         count = Counter(nums)
#         print(count)


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)  # O(n)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, f in freq.items():  # O(m) ⊆ O(n)
            buckets[f].append(num)

        ans = []
        # 가장 높은 빈도부터 내려가며 수집
        for f in range(len(nums), 0, -1):  # O(n)
            for num in buckets[f]:
                ans.append(num)
                if len(ans) == k:
                    return ans
        return ans


from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = defaultdict(int)
        for x in nums:
            freq[x] += 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for x, f in freq.items():
            buckets[f].append(x)

        ans = []
        for f in range(len(nums), 0, -1):
            for x in buckets[f]:
                ans.append(x)
                if len(ans) == k:
                    return ans
        return ans

        heap = []
        counter = {}

        for n in nums:
            counter[n] = 1 + counter.get(n, 0)

        sol = []

        for key, val in counter.items():
            heapq.heappush(heap, (-val, key))

        while len(sol) < k:
            sol.append(heapq.heappop(heap)[1])

        return sol


from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counts = Counter(nums)
        results = [
            num for num, _ in num_counts.most_common(k)
        ]  # most_common은 (num, frequnecy) 튜플 반환
        return results
