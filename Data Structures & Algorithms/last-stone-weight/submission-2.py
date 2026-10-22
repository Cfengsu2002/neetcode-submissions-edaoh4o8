class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i]=-stones[i]
        heapq.heapify(stones)
        while len(stones)>=2:
            stone1 =heapq.heappop(stones)
            stone2 =heapq.heappop(stones)
            if (stone1==stone2):
                continue
            heapq.heappush(stones, min(stone1, stone2)-max(stone1, stone2))
        return -stones[0] if stones else 0

            

            
