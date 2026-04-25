class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # use max heap and return the last value
        stone_crushers=[]
        for stone in stones:
            heapq.heappush(stone_crushers, -stone)
        while(len(stone_crushers)>1):
            stone1=-heapq.heappop(stone_crushers)
            stone2=-heapq.heappop(stone_crushers)
            if(stone1!=stone2):
                heapq.heappush(stone_crushers, -abs(stone1-stone2))
        return -stone_crushers[-1] if stone_crushers else 0