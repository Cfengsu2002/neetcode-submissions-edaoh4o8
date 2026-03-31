class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hash_map=Counter(tasks)
        max_heap=[-value for value in hash_map.values()]
        heapq.heapify(max_heap)
        time=0
        heap=deque()
        while(max_heap or heap):
            time+=1
            if max_heap:
                count=1+heapq.heappop(max_heap)
                if(count!=0):
                    heap.append([count, time+n])
            if(heap and heap[0][1]==time):
                heapq.heappush(max_heap, heap.popleft()[0])
        return time        