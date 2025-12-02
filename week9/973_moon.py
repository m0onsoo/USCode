import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for i, xy in enumerate(points):
            x, y = xy[0], xy[1]
            max_heap.append((self.E_distance(x, y), xy))
        heapq.heapify(max_heap)

        result = []
        for _ in range(k):
            result.append(heapq.heappop(max_heap)[1])
        
        return result
        

    def E_distance(self, x: int, y: int) -> int:
        # return pow(x ** 2 + y ** 2, 1/2)
        return x ** 2 + y ** 2