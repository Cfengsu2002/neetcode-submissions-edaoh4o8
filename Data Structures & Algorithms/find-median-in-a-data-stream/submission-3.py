import heapq

class MedianFinder:

    def __init__(self):
        self.max_left_heap = []   # 存负数，模拟最大堆
        self.min_right_heap = []  # 存正数，最小堆

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_left_heap, -num)

        # 保证 left 最大值 <= right 最小值
        if self.min_right_heap and -self.max_left_heap[0] > self.min_right_heap[0]:
            val = -heapq.heappop(self.max_left_heap)
            heapq.heappush(self.min_right_heap, val)

        # 保证 left 数量 >= right 数量，且最多多 1 个
        if len(self.max_left_heap) > len(self.min_right_heap) + 1:
            val = -heapq.heappop(self.max_left_heap)
            heapq.heappush(self.min_right_heap, val)

        if len(self.min_right_heap) > len(self.max_left_heap):
            val = heapq.heappop(self.min_right_heap)
            heapq.heappush(self.max_left_heap, -val)

    def findMedian(self) -> float:
        total = len(self.max_left_heap) + len(self.min_right_heap)

        if total % 2 == 1:
            return -self.max_left_heap[0]
        else:
            return (-self.max_left_heap[0] + self.min_right_heap[0]) / 2