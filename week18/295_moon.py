import heapq

# 146ms, 41.61MB
class MedianFinder:
    def __init__(self):
        # max heap 왼쪽, min heap 오른쪽
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if self.min_heap and num > self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, num * -1)
        
        if abs(len(self.min_heap) - len(self.max_heap)) >= 2:
            self.fix()

    def fix(self) -> None:    
        if len(self.max_heap) > len(self.min_heap):
            heapq.heappush(self.min_heap, heapq.heappop(self.max_heap) * -1)
        else:
            heapq.heappush(self.max_heap, heapq.heappop(self.min_heap) * -1)

    def findMedian(self) -> float:
        if (len(self.max_heap) + len(self.min_heap)) % 2 == 0:
            med = (self.max_heap[0] * -1 + self.min_heap[0]) / 2
        else:
            if len(self.max_heap) > len(self.min_heap):
                # e.g. 2 > 1
                med = self.max_heap[0] * -1
            else:
                # 1 2
                med = self.min_heap[0]
        
        return med


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()