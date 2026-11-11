import heapq
from typing import List

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        answer = [-1] * len(queries)

        query_index = []
        for i in range(len(queries)):
            query_index.append((queries[i], i))

        query_index.sort(key=lambda x: x[0])

        pq = []
        i = 0

        for query, index in query_index:
            while i < len(intervals) and intervals[i][0] <= query:
                left, right = intervals[i]
                heapq.heappush(pq, (right - left + 1, right))
                i += 1

            while pq and pq[0][1] < query:
                heapq.heappop(pq)

            if pq:
                answer[index] = pq[0][0]

        return answer

        # Time: O(n log n + m log m)
        # Space: O(n + m)
        # n = 查询数量，m = 区间数量