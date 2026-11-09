class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        pre_last=-float('inf')
        answer=0
        for i in range(len(intervals)): 
            if(intervals[i][0]>=pre_last): #2,4]>=2
                pre_last=intervals[i][1] #[2]
            else:
                answer+=1 
                pre_last=min(pre_last, intervals[i][1]) #[2]
        return answer