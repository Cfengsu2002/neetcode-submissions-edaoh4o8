import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(target):
            if(target==0):
                return False
            banan_eat_time=0
            for i in range(len(piles)):
                banan_eat_time+=math.ceil(piles[i]/target)
            return True if(banan_eat_time<=h) else False
        l_ptr=0
        ans=-1
        r_ptr=max(piles)
        while(l_ptr<=r_ptr):
            m_ptr=(l_ptr+r_ptr)//2
            if(can_finish(m_ptr)):
                r_ptr=m_ptr-1
                ans=m_ptr
            else:
                l_ptr=m_ptr+1
        return ans