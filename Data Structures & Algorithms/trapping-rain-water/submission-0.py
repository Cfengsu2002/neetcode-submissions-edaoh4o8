class Solution:
    def trap(self, height: List[int]) -> int:
        left_max=[0]*len(height)
        for i in range(1, len(left_max)):
            left_max[i]=max(height[i-1], left_max[i-1])
        right_max=[0]*len(height)
        ans=0
        for i in range(len(left_max)-2,-1,-1):
            right_max[i]=max(height[i+1], right_max[i+1])
            ans+=max(min(left_max[i], right_max[i])-height[i], 0)
        return ans 