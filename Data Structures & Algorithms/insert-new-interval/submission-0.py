class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #  intervals[i] = [start_i, end_i]
        #  start, end time of the ith interval
        # sorted ascending
        # newInterval
        # insert into intervals, still ascending order
        # order by start_i, intervals still does not have overlappintg
        # retrun intervals
        # [1:3] [4:6] = [2:5] 
        #situation 1
        #  [[1,3],[4,6]] # [2,5]
        # stack[-1][1]>insertion[0]


        # situation 2
        # [[1,2],[3,5],[6,7]] #[9,10]
        # current[0]<insertion[1]
        answer=[] # 
        for i in range(len(intervals)):
            # [4, 6], [1,6]
            if(intervals[i][0]>newInterval[1]):
                answer=answer+[newInterval]+intervals[i:]
                return answer

            elif(newInterval[0]<=intervals[i][1]):#
                newInterval[0]=min(newInterval[0], intervals[i][0])
                newInterval[1]=max(newInterval[1], intervals[i][1])
                #[]
            else:
                answer.append(intervals[i])
        return answer+[newInterval]


