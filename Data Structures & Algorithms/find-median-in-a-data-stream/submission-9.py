import heapq


class MedianFinder:

    def __init__(self):
        self.min_heap = []  
        self.max_heap = [] 
    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)
        largest = -heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, largest)
        if len(self.min_heap) > len(self.max_heap):
            smallest = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -smallest)

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2
        return -self.max_heap[0]