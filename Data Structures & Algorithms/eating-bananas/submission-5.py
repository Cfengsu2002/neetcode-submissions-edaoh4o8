import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        def banna_eat(pile):
            time=0
            for i in piles:
                time+=math.ceil(i/pile)
            return time
        while l<r:
            median_pile=(l+r)//2
            time=banna_eat(median_pile)
            if(time<=h):
                r=median_pile
            else:
                l=median_pile+1
        return r

            