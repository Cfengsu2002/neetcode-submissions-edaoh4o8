class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue=deque()
        ans=[]
        for i in range(len(nums)):
            if(i < k):
                while(queue and nums[queue[-1]]<nums[i]):
                    queue.pop()
                queue.append(i)
                if(i==k-1):
                    ans.append(nums[queue[0]])
            else:
                left_window=i-k+1
                if(queue[0]<left_window):
                    queue.popleft()
                while(queue and nums[queue[-1]]<nums[i]):
                    queue.pop()
                queue.append(i)
                ans.append(nums[queue[0]])
        return ans
                