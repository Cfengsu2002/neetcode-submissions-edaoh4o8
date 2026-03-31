class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.pq=[]
        heapq.heapify(self.pq)
        for element in nums:
            heapq.heappush(self.pq, -element)
    def add(self, val: int) -> int:
        heapq.heappush(self.pq, -val)
        copys=self.pq.copy()
        for i in range(self.k-1):
            heapq.heappop(copys)
        ans=-copys[0]
        return ans 
