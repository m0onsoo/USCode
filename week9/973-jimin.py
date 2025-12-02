# https://leetcode.com/problems/k-closest-points-to-origin/
# 973-k-closest-points-to-origin


# Idea L k closest : heap


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for x, y in points:
            distances.append(((x**2) + (y**2), [x, y]))
        heapq.heapify(distances)

        ans = []
        for i in range(k):
            ans.append(heapq.heappop(distances)[1])

        return ans

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [(-1 * ((x**2) + (y**2)), [x, y]) for x, y in points]

        heap = []
        for dist in distances[:k]:
            heapq.heappush(heap, dist)
        for dist in distances[k:]:
            if dist[0] > heap[0][0]:
                heapq.heapreplace(heap, dist)

        ans = []
        while heap:
            ans.append(heapq.heappop(heap)[1])

        return ans
