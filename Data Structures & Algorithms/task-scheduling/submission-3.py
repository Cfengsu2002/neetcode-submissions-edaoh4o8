class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_value=Counter(tasks)
        timer_task_count=[]
        for key, value in task_value.items():
            timer_task_count.append([0, value])
        
        time=0
        heapq.heapify(timer_task_count)

        while timer_task_count:
            if time<timer_task_count[0][0]:
                time+=1
                continue
            time+=1
            timer, count=heapq.heappop(timer_task_count)
            count-=1
            if count==0:
                continue
            else:
                heapq.heappush(timer_task_count, [timer+1+n, count])
        return time