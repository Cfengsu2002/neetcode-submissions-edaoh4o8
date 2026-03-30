class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans=0
        l=0
        r=len(heights)-1
        while(l<=r):
            width=r-l
            height=min(heights[l], heights[r])
            ans=max(ans, width*height)
            if heights[r]<heights[l]:
                r-=1 
            else:
                l+=1
        print(ans)
        return ans