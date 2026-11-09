"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        answer=0
        room=0
        start_time=[]
        end_time=[]
        for i in range(len(intervals)):
            start_time.append(intervals[i].start)
            end_time.append(intervals[i].end)
        start_time.sort() #[0, 5, 15] # 
        end_time.sort() #[10, 20, 40]
        start_ptr=0
        end_ptr=0
        while end_ptr<len(end_time) and start_ptr<len(start_time): # 1<3, 2<3
            if(start_time[start_ptr]<end_time[end_ptr]): #15<20
                room+=1 #2
                answer=max(answer, room) #2
                start_ptr+=1 # 3
            else:
                room-=1 # 
                end_ptr+=1
        return answer