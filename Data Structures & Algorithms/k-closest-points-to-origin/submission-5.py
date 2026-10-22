class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # key = lambda x: x[2]
        distances=[]
        for point in points:
            distances.append(((point[0])*(point[0]) + (point[1])*(point[1]), point))
        print(distances)
        heapq.heapify(distances)
        ans=[]
        for i in range(k):
            point=heapq.heappop(distances)
            point=point[1]
            ans.append(point)
        return ans