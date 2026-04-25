class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points_pq=[]
        for point in points:
            x,y=point
            distance=x*x+y*y
            heapq.heappush(points_pq, (distance, (x,y)))
        print(points_pq)
        ans=[]
        for i in range(k):
            distance, location=heapq.heappop(points_pq)
            ans.append(location)
        return ans 
