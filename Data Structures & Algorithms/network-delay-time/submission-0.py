class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # construct the graph
        node_distance_next=defaultdict(list)
        for i in range(len(times)):
            cur_node, next_node, distance=times[i][0], times[i][1], times[i][2]
            node_distance_next[cur_node].append([distance, next_node])
        print(node_distance_next)
        # construct priority_heap
        visited_node=set()
        visited_node.add(k)
        distance_next_queue=[]
        for i in range(len(node_distance_next[k])):
            distance=node_distance_next[k][i][0]
            next_node=node_distance_next[k][i][1]
            distance_next_queue.append([distance, next_node])
        
        # initial the queue
        longest_time_reach=0
        heapq.heapify(distance_next_queue)
        print(distance_next_queue)
        while(distance_next_queue):
            cur_time, cur_node = heapq.heappop(distance_next_queue)
            if(cur_node in visited_node):
                continue
            longest_time_reach=cur_time
            for time, next_node in node_distance_next[cur_node]:
                time+=cur_time
                heapq.heappush(distance_next_queue,[time,next_node])
            visited_node.add(cur_node)
        return longest_time_reach if(len(visited_node)==n) else -1

                





